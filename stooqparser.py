import csv
import urllib.request

def stock_share(stock_code):
    target_url = 'https://stooq.com/q/l/?s=' + stock_code + '&f=sd2t2ohlcv&h&e=csv'
    response = urllib.request.urlopen(target_url)
    csv_data = csv.reader(line.decode() for line in response)
    
    line_count = 0
    for row in csv_data:
        if line_count == 1:
            symbol = row[0]
            closePerShare = row[-2]
            if closePerShare == 'N/D':
                raise Exception('No data!')
            message = symbol + ' quote is $' + closePerShare + ' per share'
            return message
        line_count += 1

stock_code_apple= 'appl.us'