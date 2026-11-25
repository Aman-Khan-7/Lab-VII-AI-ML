import numpy as np
from sklearn.metrics import accuracy_score

# True labels (0 = Not Spam, 1 = Spam)
y_true_spam = np.array([0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0])
# Predicted labels by your model
y_pred_spam = np.array([0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0])

print("True Spam Labels:", y_true_spam)
print("Predicted Spam Labels:", y_pred_spam)

accuracy = accuracy_score(y_true_spam, y_pred_spam)
print(f"Classification Accuracy: {accuracy:.2f} ({accuracy * 100:.1f}%)")
