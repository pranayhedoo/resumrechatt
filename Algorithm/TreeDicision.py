from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# New Dataset
data = {
    'Age': [22, 28, 35, 42, 55],
    'Income': [40000, 50000, 70000, 110000, 95000],
    'Buys_Computer': ['No', 'No', 'Yes', 'Yes', 'Yes']
}

# Creating DataFrame
df = pd.DataFrame(data)
print(df)

# Splitting features and target
X = df[['Age', 'Income']]  # Input features
y = df['Buys_Computer']    # Target variable

# Model training
model = DecisionTreeClassifier()
model.fit(X, y)

# Prediction for new data
new_data = pd.DataFrame({'Age': [38], 'Income': [85000]})
prediction = model.predict(new_data)

# Output the prediction
print("Prediction:", prediction[0])
