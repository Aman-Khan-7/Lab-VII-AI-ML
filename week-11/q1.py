import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split

np.random.seed(0)
X = np.sort(5 * np.random.rand(80, 1), axis=0)
y = np.sin(X).ravel() + np.random.normal(0, 0.5, 80)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Underfitting (Linear Model)
lin_model = LinearRegression()
lin_model.fit(X_train, y_train)
y_pred_lin = lin_model.predict(X_test)

plt.scatter(X_train, y_train, label='Train')
plt.scatter(X_test, y_test, label='Test', alpha=0.6)
plt.plot(X, lin_model.predict(X), color='red', label='Linear Fit (Underfit)')
plt.title("Underfitting: Linear Regression")
plt.legend()
plt.show()

# Overfitting (Degree-20 Polynomial Model)
poly_model = make_pipeline(PolynomialFeatures(degree=20), LinearRegression())
poly_model.fit(X_train, y_train)
y_pred_poly = poly_model.predict(X_test)

X_plot = np.linspace(0, 5, 200).reshape(-1, 1)
plt.scatter(X_train, y_train, label='Train')
plt.scatter(X_test, y_test, label='Test', alpha=0.6)
plt.plot(X_plot, poly_model.predict(X_plot), color='green', label='Degree 20 Fit (Overfit)')
plt.ylim(-3, 3)
plt.title("Overfitting: Degree-20 Polynomial")
plt.legend()
plt.show()
