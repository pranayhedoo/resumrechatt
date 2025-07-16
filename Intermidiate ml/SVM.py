import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

# Step 1: Prepare the data points and their classes
X = np.array([[1, 0.5], [1, 1], [1, -0.5], [-0.5, 0.5], [2, 0],
              [4, 0], [4.5, 1], [4.5, -0.5], [5, -1], [5.5, 0]])

# Assume class labels for demonstration
y = [-1, -1, -1, -1, -1, 1, 1, 1, 1, 1]  # You can adjust based on actual classification

# Step 2: Create SVM model
model = svm.SVC(kernel='linear')

# Step 3: Fit the model
model.fit(X, y)

# Step 4: Plotting
plt.scatter(X[:, 0], X[:, 1], c=y)
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# Plot decision boundary
xx = np.linspace(xlim[0], xlim[1])
yy = np.linspace(ylim[0], ylim[1])
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = model.decision_function(xy).reshape(XX.shape)

ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
            linestyles=['--', '-', '--'])

plt.show()

# Output hyperplane parameters
print("Weights:", model.coef_)
print("Bias:", model.intercept_)