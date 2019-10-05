import csv
import urllib.request

stock_code = 'aapl.us'

def stock_share_parser(stock_code):
    target_url = 'https://stooq.com/q/l/?s=' + stock_code + '&f=sd2t2ohlcv&h&e=csv'
    response = urllib.request.urlopen(target_url)
    csv_data = csv.reader(line.decode() for line in response)
    
    line_count = 0
    for row in csv_data:
        if line_count == 1:
            stock_quote_message = row[0] + " quote is $" + row[-2] + " per share"
            return stock_quote_message
    line_count += 1