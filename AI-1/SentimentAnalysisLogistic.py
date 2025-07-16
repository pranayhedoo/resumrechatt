from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Step 1: Sample dataagi
texts = ["I love it", "I hate it", "Very good", "Very bad"]
labels = [1, 0, 1, 0]  # 1 = Positive, 0 = Negative

# Step 2: Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Step 3: Train logistic regression model
model = LogisticRegression()
model.fit(X, labels)

# Step 4: Predict new text
test = ["I love this", "This is bad"]
test_X = vectorizer.transform(test)
pred = model.predict(test_X)

# Step 5: Print result
for t, p in zip(test, pred):
    print(f"{t} → {'Positive' if p == 1 else 'Negative'}")
