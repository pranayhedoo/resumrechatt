from sklearn.cluster import AgglomerativeClustering
import numpy as np

# Example Data: Simple 2D points
X = np.array([[1, 2], [2, 3], [3, 3], [8, 8], [9, 9], [10, 10]])

# Apply Hierarchical Clustering with 2 clusters
hc = AgglomerativeClustering(n_clusters=2)
labels = hc.fit_predict(X)

print("Cluster Labels:", labels)

