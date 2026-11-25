from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
iris_df = iris.frame

features = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
X = iris_df[features]

# Min-Max Normalization (0 to 1)
X_normalized = (X - X.min()) / (X.max() - X.min())
print("Normalized Features (first 5 rows):\n", X_normalized.head())

# Z-score Standardization (mean=0, std=1)
X_standardized = (X - X.mean()) / X.std()
print("\nStandardized Features (first 5 rows):\n", X_standardized.head())
