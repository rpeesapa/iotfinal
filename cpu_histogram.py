import numpy as np
import matplotlib.pyplot as plt
import pylab as P
import pdb
from pandas import *
data = read_csv('iotfinal - Sheet1.csv')
x = data['CPU Usage']
num_bins = 30
n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='blue', alpha=0.5)
plt.xlabel('CPU Usage %')
plt.ylabel('probability')
plt.title('Histogram of CPU Usage %')
plt.grid(True)
plt.show()
