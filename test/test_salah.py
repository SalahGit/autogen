#python code
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd

# Download stock data
nvda = yf.download('NVDA', start='2022-01-01', end=pd.to_datetime('today').strftime('%Y-%m-%d'))
tesla = yf.download('TSLA', start='2022-01-01', end=pd.to_datetime('today').strftime('%Y-%m-%d'))

# Plot the close prices
plt.figure(figsize=(14, 7))
plt.plot(nvda['Close'], label='NVDA')
plt.plot(tesla['Close'], label='TESLA')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.title('NVDA vs TESLA Stock Price YTD')
plt.legend()
plt.grid(True)
plt.show()