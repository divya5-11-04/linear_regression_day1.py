import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

X = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([1,2,2,4,5])

model = LinearRegression()
model.fit(X,y)

y_pred = model.predict(X)

print("coefficients",model.coef_)
print("Intercept:",model.intercept_)
print("MSE:",mean_squared_error(y,y_pred))

plt.scatter(X,y,color="blue")
plt.plot(X,y_pred,color="red")
plt.title('Linear Regression Line')
plt.show()