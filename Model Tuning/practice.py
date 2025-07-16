from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

iris = load_iris()
X = iris.data
y = iris.target

model = DecisionTreeClassifier()

# Hyperparameter options to try
param_grid = {
    'max_depth': [2, 3, 4, 5],
    'min_samples_split': [2, 3, 4]
}

grid_search = GridSearchCV(model, param_grid, cv=3)  # 3-fold cross-validation
grid_search.fit(X, y)

print("Best Parameters:", grid_search.best_params_)
