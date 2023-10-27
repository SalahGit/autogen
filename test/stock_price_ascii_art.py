# filename: stock_price_ascii_art.py
import yfinance as yf
import pandas as pd
from yahoo_fin import stock_info as si
from datetime import datetime, timedelta
from artplotlib import AsciiChart

# Get today's date and the date one year ago
today = datetime.today().strftime('%Y-%m-%d')
year_ago = (datetime.today()-timedelta(days=365)).strftime('%Y-%m-%d')

# Download historical market data
hist_NVDA = yf.download('NVDA', start=year_ago, end=today)
hist_TSLA = yf.download('TSLA', start=year_ago, end=today)

# Calculate the YTD price change
hist_NVDA['YTD Change'] = hist_NVDA['Close'].pct_change()
hist_TSLA['YTD Change'] = hist_TSLA['Close'].pct_change()

# Prepare data for ascii chart
data_NVDA = hist_NVDA['YTD Change'].dropna().tolist()
data_TSLA = hist_TSLA['YTD Change'].dropna().tolist()

# Create ascii charts
chart_NVDA = AsciiChart()
chart_NVDA.add_data(data_NVDA, label='NVDA')
print("\nNVDA stock price change YTD\n")
chart_NVDA.render()

chart_TSLA = AsciiChart()
chart_TSLA.add_data(data_TSLA, label='TSLA')
print("\nTSLA stock price change YTD\n")
chart_TSLA.render()