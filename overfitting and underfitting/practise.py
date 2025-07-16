import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Create sample data
np.random.seed(0)
x = np.linspace(0, 10, 30)
y = np.sin(x) + np.random.normal(0, 0.1, size=x.shape)  # Adding some noise

# Create x for prediction
x_test = np.linspace(0, 10, 100)

# Underfitting: Linear Model (Degree 1)
model_underfit = make_pipeline(PolynomialFeatures(degree=1), LinearRegression())
model_underfit.fit(x.reshape(-1, 1), y)
y_underfit = model_underfit.predict(x_test.reshape(-1, 1))

# Overfitting: High-Degree Polynomial (Degree 15)
model_overfit = make_pipeline(PolynomialFeatures(degree=15), LinearRegression())
model_overfit.fit(x.reshape(-1, 1), y)
y_overfit = model_overfit.predict(x_test.reshape(-1, 1))

# Good Fit: Proper Complexity (Degree 4)
model_goodfit = make_pipeline(PolynomialFeatures(degree=4), LinearRegression())
model_goodfit.fit(x.reshape(-1, 1), y)
y_goodfit = model_goodfit.predict(x_test.reshape(-1, 1))

# Plot all three
plt.figure(figsize=(18, 5))

# Underfitting Plot
plt.subplot(1, 3, 1)
plt.scatter(x, y, color='black', label='Data')
plt.plot(x_test, y_underfit, color='red', label='Underfitting')
plt.title('Underfitting (Linear)')
plt.legend()

# Overfitting Plot
plt.subplot(1, 3, 2)
plt.scatter(x, y, color='black', label='Data')
plt.plot(x_test, y_overfit, color='green', label='Overfitting')
plt.title('Overfitting (Degree 15)')
plt.legend()

# Good Fit Plot
plt.subplot(1, 3, 3)
plt.scatter(x, y, color='black', label='Data')
plt.plot(x_test, y_goodfit, color='blue', label='Good Fit')
plt.title('Good Fit (Degree 4)')
plt.legend()

plt.show()
