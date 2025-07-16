# # Importing necessary libraries
# from sklearn.neighbors import KNeighborsClassifier
# import numpy as np

# # Sample data: Hours studied vs Pass (1) or Fail (0)
# X = np.array([[1], [2], [3], [4], [5], [6]])  # Feature: Hours studied
# y = np.array([0, 0, 0, 1, 1, 1])              # Target: Pass (1) or Fail (0)

# # Creating KNN model with K = 3
# model = KNeighborsClassifier(n_neighbors=3)

# # Training the model
# model.fit(X, y)

# # Predicting for a new student who studied 3.5 hours
# prediction = model.predict([[3.5]])
# print("Predicted Class (1 = Pass, 0 = Fail):", prediction[0])

from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# New data: Weight of fruit vs Fruit Type (0 = Apple, 1 = Orange)
X = np.array([[100], [150], [200], [250], [300], [350]])  # Weight of fruit in grams
y = np.array([0, 0, 1, 1, 1, 0])                         # 0 = Apple, 1 = Orange

# Create KNN model with K = 3
model = KNeighborsClassifier(n_neighbors=3)

# Train the model
model.fit(X, y)

# Predict for a fruit that weighs 240 grams
prediction = model.predict([[240]])
print("Predicted Class (0 = Apple, 1 = Orange):", prediction[0])
