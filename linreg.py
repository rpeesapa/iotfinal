import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from pandas import read_csv
data = read_csv('iotfinal - Sheet1.csv')
x = data['CPU Usage']
y = data['Temperature C']
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
l = [slope * i + intercept for i in x]
plt.xlabel('CPU Usage %')
plt.ylabel('Temperature C')
plt.plot(x,y,'bo')
plt.plot(x,l,'red')
plt.show()