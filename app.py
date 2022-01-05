import pandas as pd
import requests
import json

key = 'XXX'
ticker = 'AAPL'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&apikey={}'.format(ticker, key)
response = requests.get(url)
print(response.json())

# example for later https://github.com/jiayi-ren/stock-scraper/blob/master/scraper.py
