import os 
import streamlit as st
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime
from bokeh.plotting import figure

st.set_page_config(page_icon="📈", layout="wide")
st.title("Day 10 Milestone Project")
st.subheader("by Nancy Williams")
st.write('This app demonstrates pulling stock data from Alpha Advantage via an API and displaying using Streamlit, Pandas, and Bokeh on a Heroku app.')
st.caption("*Note that these values are unadjusted, meaning that they do not correct for splits. Looking at the stock's trends over long periods of time can be misleading. The adjusted data are a premium feature.")

# Need to set default ticker to something like AAPL
st.sidebar.header('Set plot parameters:')
ticker='MSFT'
if st.sidebar.text_input("Enter the stock's abbreviation (e.g. MSFT):", key='ticker'):
     ticker = st.session_state.ticker

# Help at https://devcenter.heroku.com/articles/config-vars
# API key must be named ALPHAVANTAGE_API_KEY
ts = TimeSeries(output_format='pandas')
try: 
     data, meta_data = ts.get_daily(ticker, outputsize='full')
except NameError:
     st.error('The API call has failed because that ticker does not exist.')

st.sidebar.write("Select the time period you wish to plot:")
period = st.sidebar.slider('Date Range',
     value=[datetime(1999,9,1), datetime(2022,4,1)])

# Plot the data
p = figure(
     #title='simple line example',
     x_axis_label='Time',
     x_axis_type='datetime',
     y_axis_label='Price ($)',
     x_range=period,
     title=ticker)

p.title.text_font_size = '20pt'
p.line(data.index, data['4. close'], 
     legend_label='Closing', 
     line_width=1.5)
st.bokeh_chart(p, use_container_width=True)
# example https://docs.streamlit.io/library/api-reference/charts/st.bokeh_chart

# show dataframe for funsies
if st.checkbox('Show raw data'):
    data