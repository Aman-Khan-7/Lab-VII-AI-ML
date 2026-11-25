import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X_shapes = np.array([
    [4, 1.0], [4, 1.05], [4, 0.95],
    [0, 1.0], [0, 1.1], [0, 0.9],
    [4, 0.5], [0, 2.0]
])
y_shapes = np.array([0, 0, 0, 1, 1, 1, 0, 1])

X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
    X_shapes, y_shapes, test_size=0.3, random_state=42
)

mlp = MLPClassifier(hidden_layer_sizes=(5,), max_iter=500, random_state=42, solver='adam')
mlp.fit(X_train_s, y_train_s)

y_pred_s = mlp.predict(X_test_s)
print("MLP Accuracy:", accuracy_score(y_test_s, y_pred_s))
