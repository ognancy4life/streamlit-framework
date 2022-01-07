import os
import streamlit as st
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

st.text_input("Enter the stock's abbreviation (all capital letters):", key='ticker')
# You can access the value at any point with: st.session_state.ticker

st.write("Select the time period you wish to plot:")
neighborhood = st.radio("Time Period", ['1 day', '1 week', '1 month', '1 year'])

key = os.environ.get('KEY')
ticker = st.session_state.ticker
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey={}'.format(ticker, key)
#response = requests.get(url)
df = pd.read_json(url)
st.write(df)
st.write(df['Time Series (Daily)'].apply(lambda row: glom(row, '4. close')))
#print(response.json())
#st.write(response.json())

# example for later https://github.com/jiayi-ren/stock-scraper/blob/master/scraper.py
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
     title='simple line example',
     x_axis_label='x',
     y_axis_label='y')

p.line(x, y, legend_label='Trend', line_width=2)

st.bokeh_chart(p, use_container_width=True)
