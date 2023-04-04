import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

stock_data = yf.download('MSFT', start='2010-01-01', end='2023-04-01')

stock_data['Daily Return'] = stock_data['Adj Close'].pct_change()
stock_data['SMA'] = stock_data['Adj Close'].rolling(window=50).mean()

stock_data['Position'] = [1 if stock_data['Adj Close'][i] > stock_data['SMA'][i] else 0 for i in range(len(stock_data))]
stock_data['Position'] = stock_data['Position'].shift(1)
stock_data['Position'].fillna(method='ffill', inplace=True)
stock_data['Returns'] = stock_data['Position'] * stock_data['Daily Return']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.arange(len(stock_data))
y = stock_data['Adj Close']
z = stock_data['Position']

ax.plot(x, y, z)
ax.set_xlabel('Days')
ax.set_ylabel('closing price')
ax.set_zlabel('Position')

plt.show()
