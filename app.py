import os 
import streamlit as st
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import requests
import json
from glom import glom
from bokeh.plotting import figure

st.title("Day 10 Milestone Project")
st.header("by Nancy Williams")
st.write('This app demonstrates pulling stock data from Alpha Advantage via an API and displaying using Streamlit, Pandas, and Bokeh on a Heroku app.')
# st.header("Customary quote")
# st.markdown("> I just love to go home, no matter where I am [...]")

# Need to set default ticker to something like AAPL
st.text_input("Enter the stock's abbreviation (all capital letters):", key='ticker')
# You can access the value at any point with: st.session_state.ticker

st.write("Select the time period you wish to plot:")
neighborhood = st.radio("Time Period", ['1 day', '1 week', '1 month', '1 year'])

#ALPHAVANTAGE_API_KEY = os.environ['ALPHAVANTAGE_API_KEY']
#st.write(ALPHAVANTAGE_API_KEY)
ts = TimeSeries(output_format='pandas')

ticker = st.session_state.ticker
data, meta_data = ts.get_intraday(ticker)

#url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey={}&datatype=csv'.format(ticker, key)
#response = requests.get(url)
# data = response.json()
#with open(str(data),'r') as f:
#    data2 = json.loads(f.read())
    
#df = pd.json_normalize(
#    data['Time Series (Daily)'],
#    meta='Meta Data'
#    ).T
#df = pd.read_json(data, orient='records')
st.write(data)
#st.write(df['Time Series (Daily)'].apply(lambda row: glom(row, '4. close')))
#print(response.json())
#st.write(response.json())

# Need to figure out how to get only fields including "close" and parse the dates

# example for later https://github.com/jiayi-ren/stock-scraper/blob/master/scraper.py
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
     title='simple line example',
     x_axis_label='x',
     y_axis_label='y')

p.line(x, y, legend_label='Trend', line_width=2)

st.bokeh_chart(p, use_container_width=True)
