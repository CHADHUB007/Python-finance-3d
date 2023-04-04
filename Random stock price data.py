import pandas as pd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# We generate some sample data
n = 1000
data = pd.DataFrame({'Price': np.random.normal(100, 10, n)})

# Calculate the 50-day moving average
data['moving_average'] = data['Price'].rolling(50).mean()

# We assign the buy (1) or sell (-1) position based on the described strategy
data['Position'] = np.where(data['Price'] > data['moving_average'], 1, -1)


# Calculate the performance of the strategy
data['Perfomance'] = data['Position'].shift(1) * (data['Price'] - data['Price'].shift(1))


# We plot the strategy and the moving average in 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data.index, data['Price'], data['Perfomance'], c=data['Position'])
ax.plot(data.index, data['moving_average'], zs=0, zdir='y', color='red')
ax.set_xlabel('Day')
ax.set_ylabel('Price')
ax.set_zlabel('Performance')
plt.show()
