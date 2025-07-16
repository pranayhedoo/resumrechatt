from sklearn.cluster import DBSCAN
import numpy as np

# Example Data: Simple 2D points
X = np.array([[1, 2], [2, 2], [2, 3], [8, 7], [8, 8], [25, 80]])

# Apply DBSCAN
dbscan = DBSCAN(eps=1.5, min_samples=2)  # eps: radius, min_samples: minimum neighbors
labels = dbscan.fit_predict(X)

print("Cluster Labels:", labels)
