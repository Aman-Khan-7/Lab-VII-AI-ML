import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

np.random.seed(42)
small_animals = np.random.normal(loc=[5, 20], scale=[1, 5], size=(20, 2))
medium_animals = np.random.normal(loc=[50, 80], scale=[10, 15], size=(20, 2))
large_animals = np.random.normal(loc=[300, 150], scale=[50, 25], size=(20, 2))

X_animals = pd.DataFrame(
    np.vstack([small_animals, medium_animals, large_animals]),
    columns=['Weight_kg', 'Height_cm']
)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_animals)
X_scaled_df = pd.DataFrame(X_scaled, columns=X_animals.columns)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X_scaled_df)
X_animals['Cluster'] = kmeans.labels_

centroids = scaler.inverse_transform(kmeans.cluster_centers_)

plt.scatter(X_animals['Weight_kg'], X_animals['Height_cm'], c=X_animals['Cluster'], cmap='viridis', label='Animals')
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.title("Animal Clusters (K-Means)")
plt.xlabel("Weight (kg)")
plt.ylabel("Height (cm)")
plt.legend()
plt.show()
# A centroid is the average center point of all data points in a cluster.
