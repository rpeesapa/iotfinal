import numpy as np
import matplotlib.pyplot as plt
import pdb
from pandas import *
data = read_csv('iotfinal - Sheet1.csv')
x = data['CPU Usage']
y = data['Temperature C']
t = data['Index']
plt.plot(t,x,'b',label = 'CPU Usage %')
plt.plot(t,y,'r',label='Temperature C')

plt.xlabel('Date/Time')
plt.ylabel('Temperature C')
plt.title('Time Series')
legend = plt.legend(loc='upper left', shadow=True, fontsize='x-large')
legend.get_frame().set_facecolor('#00FFCC')

plt.grid(True)
plt.show()