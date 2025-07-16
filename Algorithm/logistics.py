# import pandas as pd
# from sklearn.linear_model import LogisticRegression
# data = {
#  'Age': [25, 32, 28, 45, 29],
#  'Income': [25000, 50000, 30000, 70000, 40000],
#  'Approved': [0, 1, 0, 1, 0]
#  }
# X = df[['Age', 'Income’]]
# y = df['Approved']
# model = LogisticRegression()
# model.fit(X, y)

# import pandas as pd
# from sklearn.linear_model import LogisticRegression

# # Creating the dataset
# data = {
#     'Age': [25, 32, 28, 45, 29],
#     'Income': [25000, 50000, 30000, 70000, 40000],
#     'Approved': [0, 1, 0, 1, 0]
# }

# # Converting to DataFrame
# df = pd.DataFrame(data)

# # Independent variables (features)
# X = df[['Age', 'Income']]

# # Dependent variable (target)
# y = df['Approved']

# # Create and train logistic regression model
# model = LogisticRegression()
# model.fit(X, y)

# # Predicting for a new applicant
# new_applicant = [[34, 55000]]
# prediction = model.predict(new_applicant)
# probability = model.predict_proba(new_applicant)

# # Output
# print("Prediction:", "Yes" if prediction[0] == 1 else "No")
# print("Probability of Approval:", round(probability[0][1] * 100, 2), "%")

from sklearn.linear_model import LogisticRegression
import numpy as np

# New Data: Hours studied vs Pass (1) or Fail (0)
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])  # Hours studied
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])                 # 0 = Fail, 1 = Pass

# Create and train logistic regression model
model = LogisticRegression()
model.fit(X, y)

# Predict for 4.5 hours of study
prediction = model.predict([[5.5]])
print("Prediction (0=Fail, 1=Pass):", prediction[0])
