import numpy as np
import matplotlib.pyplot as plt
from pandas import *
data = read_csv('iotfinal - Sheet1.csv')
x = data['CPU Usage']
y = data['Temperature C']
plt.figure()
plt.boxplot(x,0,'black',0)

plt.xlabel('CPU Usage %')

plt.title('Horizontal Box Plot of CPU Usage %')

plt.grid(True)
plt.show()
