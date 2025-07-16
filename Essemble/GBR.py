from sklearn.ensemble import GradientBoostingRegressor

 # Data
X = [[5], [10], [15], [20], [25]]  # Number of practice problems solved
y = [2, 4, 6, 8, 10]  # Corresponding number of hours studied

 # Model
model = GradientBoostingRegressor()
model.fit(X, y)
 # Predict
print(model.predict([[12]]))  # some changes for x y values  not in sq feet and price any more