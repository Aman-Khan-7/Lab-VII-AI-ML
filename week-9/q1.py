import numpy as np

X_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_and = np.array([0, 0, 0, 1])

np.random.seed(42)
weights = np.random.rand(2) * 0.1
bias = np.random.rand(1)[0] * 0.1

def step_function(z):
    return 1 if z >= 0 else 0

learning_rate = 0.1
epochs = 20

for epoch in range(epochs):
    for x, y_true in zip(X_and, y_and):
        z = np.dot(x, weights) + bias
        prediction = step_function(z)
        error = y_true - prediction
        weights = weights + learning_rate * error * x
        bias = bias + learning_rate * error

print("AND Gate Predictions:")
for x in X_and:
    z = np.dot(x, weights) + bias
    print(f"Input: {x} -> Predicted: {step_function(z)}")
