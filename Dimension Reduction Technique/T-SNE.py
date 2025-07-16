# t-SNE Example
from sklearn.manifold import TSNE

import matplotlib.pyplot as plt

from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target

# Apply t-SNE (reduce to 2 components)
tsne = TSNE(n_components=2, random_state=42)
X_tsne = tsne.fit_transform(X)

# Plot the results
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=y, cmap='viridis')
plt.title('t-SNE - Iris Dataset')
plt.xlabel('t-SNE Component 1')
plt.ylabel('t-SNE Component 2')
plt.show()
