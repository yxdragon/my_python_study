import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import median_filter
'''
arr = np.loadtxt('ft.dat', skiprows=1)
newy = median_filter(arr[:,1], 3)
print(arr[:,1].mean())
plt.plot(arr[:,0], arr[:,1], 'g-o')
plt.plot(arr[:,0], newy, 'r-o')
plt.plot(arr[:,0], newy*0+newy.mean(), 'b', lw=3)
plt.show()
'''

import pandas as pd

df = pd.read_csv('coins.csv')
