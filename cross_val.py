from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
import matplotlib.pyplot as plt
from pandas import read_csv
data = read_csv('iotfinal - Sheet1.csv')
x = data['CPU Usage']
y = data['Temperature C']
t = data['Index']
lasso = linear_model.Lasso()


# cross_val_predict returns an array of the same size as `y` where each entry
# is a prediction obtained by cross validated:
predicted = cross_val_predict(lasso,data, y, cv=10)

fig, ax = plt.subplots()
ax.scatter(y, predicted,c= 'red')
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'blue', lw=2)
ax.set_xlabel('Temperature C')
ax.set_ylabel('Predicted')
plt.title('Cross-Validation using Time and CPU Usage')
plt.show()