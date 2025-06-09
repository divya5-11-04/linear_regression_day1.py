# linear_regression_day1.py
# 📈 Linear Regression – Day 1 of AI Engineer Journey

## 🔍 What is Linear Regression?

Linear Regression is a **supervised machine learning algorithm** used for predicting a continuous value based on input features. It assumes a linear relationship between input variable(s) `X` and the output variable `y`.

In simple terms, it tries to fit a straight line (`y = mx + c`) that best represents the relationship between the data points.

---

## 🧠 Where is it Used?

- Predicting **house prices** based on area, location, etc.
- Estimating **sales** or **revenue** based on past trends
- **Forecasting demand**, temperatures, stock prices (basic version)
- **Analyzing relationships** in scientific data

---

## 📚 What I Learned Today

- The theory behind Linear Regression and the cost function (Mean Squared Error)
- How gradient descent is used to minimize error
- Implemented a simple Linear Regression model using:
  - `NumPy` for manual understanding
  - `scikit-learn` for real-world usage
- Visualized the regression line using `matplotlib`
- Calculated and formatted MSE (Mean Squared Error) with `.2f` precision
- Pushed my work to GitHub and wrote this README to document it
  
## 📌 Sample Code Highlight
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y)
print(f"MSE: {mean_squared_error(y, model.predict(X)):.2f}")
