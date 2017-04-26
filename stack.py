import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import math

# Original "data set" --- 21 random numbers between 0 and 1.
x0 = np.arange(9)
y0 = [math.sin(i) for i in x0]

plt.plot(x0, y0, 'o', label='Data')
plt.grid(linestyle="-", color=(0.7, 0.8, 1.0))

x = np.linspace(0, 8, 1000)

# Available options for interp1d
options = ('linear', 'nearest')

f = interp1d(x0, y0, kind='nearest')    # interpolation function
plt.plot(x, f(x), '-', label='nearest')      # plot of interpolated data

plt.legend()
plt.show()