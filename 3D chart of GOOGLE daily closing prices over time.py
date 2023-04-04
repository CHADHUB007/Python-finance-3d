import yfinance as yf
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

stock_data = yf.download("GOOGL", start="2010-01-01", end="2023-04-01")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.arange(len(stock_data))
y = stock_data['Close']
z = np.zeros(len(stock_data))

ax.plot(x, y, z)
ax.set_xlabel('Days')
ax.set_ylabel('closing price')
ax.set_zlabel('')

plt.show()
