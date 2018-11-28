import numpy as np
import matplotlib.pyplot as plt
from pandas import *
data = read_csv('iotfinal - Sheet1.csv')
x = data['Temperature C']
plt.figure()
plt.boxplot(x)

plt.xlabel('CPU Usage %')

plt.title('Vertical Box Plot of Temperature C')

plt.grid(True)
plt.show()

