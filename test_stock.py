import pytest
from stooqparser import stock_share

def test_symbol():
    assert stock_share('aapl.us'), 'Test failed'
    assert stock_share('ecuador'), 'Test failed'