
# from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt
# import numpy as np
#  # Data: Hours studied vs Exam score
# X = np.array([[1], [2], [3], [4], [5]])  # Hours
# y = np.array([10, 20, 30, 40, 50])       
# model = LinearRegression()
# model.fit(X, y)
#  # Predict score for 6 hours
#  # Scores
# predicted_score = model.predict([[6]])
# print("Predicted score:", predicted_score[0])

# # Import required libraries
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

# # Step 1: Prepare the data
# house_size = np.array([500, 1000, 1500, 2000, 2500]).reshape(-1, 1)  # Feature (X)
# house_price = np.array([50, 100, 150, 200, 250])  # Target (y)

# # Step 2: Create and train the model
# model = LinearRegression()
# model.fit(house_size, house_price)

# # Step 3: Make a prediction
# predicted_price = model.predict([[1800]])
# print(f"Predicted Price for 1800 sq ft house: ₹{predicted_price[0]:.2f} Lakhs")

# # Step 4: Visualize the result
# plt.scatter(house_size, house_price, color='blue', label='Actual Data')
# plt.plot(house_size, model.predict(house_size), color='red', label='Best Fit Line')
# plt.xlabel('House Size (sq ft)')
# plt.ylabel('Price (₹ Lakhs)')
# plt.title('Linear Regression: House Price Prediction')
# plt.legend()
# plt.show()

# from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt
# import numpy as np

# # Data: Hours studied vs Exam score
# X = np.array([[1], [2], [3], [4], [5]])  # Hours
# y = np.array([10, 20, 30, 40, 50])       # Exam Scores

# # Create and train the model
# model = LinearRegression()
# model.fit(X, y)

# # Predict score for 6 hours
# predicted_score = model.predict([[6]])
# print("Predicted score:", predicted_score[0])

# # Plot scatter chart for original data
# plt.scatter(X, y, color='blue', label='Actual Scores')

# # Plot the regression line
# plt.plot(X, model.predict(X), color='red', label='Best Fit Line')

# # Plot the predicted point
# plt.scatter(6, predicted_score[0], color='green', label='Predicted Score (6 hrs)', marker='x', s=100)

# # Add labels and legend
# plt.xlabel('Hours Studied')
# plt.ylabel('Exam Score')
# plt.title('Linear Regression: Hours Studied vs Exam Score')
# plt.legend()
# plt.grid(True)
# plt.show()

from sklearn.linear_model import LinearRegression
import numpy as np

# New Data: Temperature vs Ice Cream Sales
X = np.array([[20], [25], [30], [35], [40]])  # Temperature in °C
y = np.array([40, 60, 70, 80, 100])           # Ice Cream Sales

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict ice cream sales at 32°C
predicted_sales = model.predict([[30]])
print("Predicted ice cream sales at 32°C:", predicted_sales[0])
