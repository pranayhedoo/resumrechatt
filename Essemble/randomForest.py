# Import libraries
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))   # calculation:- accuracy_score = 42 / 45 ≈ 0.9333


# from sklearn.datasets import make_classification
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score, confusion_matrix
# import pandas as pd

# # 1. Create synthetic data
# X, y = make_classification(n_samples=500, n_features=6,
#                            n_informative=4, n_classes=2,
#                            random_state=0)

# # 2. Split data into train/test sets
# X_train, X_test, y_train, y_test = train_test_split(
#     X, y, test_size=0.2, random_state=0)

# # 3. Train the Random Forest
# clf = RandomForestClassifier(n_estimators=100,
#                              random_state=0)
# clf.fit(X_train, y_train)

# # 4. Predict & evaluate
# y_pred = clf.predict(X_test)
# print("Accuracy:", accuracy_score(y_test, y_pred))
# print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))
