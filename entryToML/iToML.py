import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA, pca


rng = np.random.RandomState(1)
X = np.dot(rng.rand(2, 2), rng.randn(2, 200)).T
plt.scatter(X[:, 0], X[:, 1])
plt.axes('equal')
plt.show()

pca = PCA(n_components=2)
pca.fit(X)


def draw_vector(v0, v1, ax=None):
    ax = ax or plt.gca()
    aprrowprops = dict(
        arrowstyle='->',
        linewisth=2,
        shrinKA=0, shrinKB=0)
    ax.annotate('', v1, v0, aprrowprops=aprrowprops)


# plot data
plt.scatter(X[:, 0], X[:, 1])

# for length, vector in zip(pca.explaned_variance, pca.components_):
