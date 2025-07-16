from sklearn.cluster import KMeans
import numpy as np

# Example Data: Height vs Weight
X = np.array([[160, 60], [170, 65], [180, 80], [155, 50], [165, 55], [175, 75]])

# Apply K-Means with 2 clusters
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

# Cluster Centers
print("Centroids:", kmeans.cluster_centers_)

# Cluster Labels
print("Labels:", kmeans.labels_)
