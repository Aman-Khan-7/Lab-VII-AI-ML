import pandas as pd
import numpy as np
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

np.random.seed(0)
churn_data = pd.DataFrame({
    'MonthlyCharges': np.random.uniform(20, 100, 200),
    'DataUsageGB': np.random.uniform(10, 80, 200),
    'ContractYears': np.random.randint(1, 4, 200),
    'Churn': np.random.choice([0, 1], 200, p=[0.7, 0.3])
})
X = churn_data.drop('Churn', axis=1)
y = churn_data['Churn']

kf = KFold(n_splits=5, shuffle=True, random_state=42)
model = LogisticRegression()
fold_accuracies = []

for fold, (train_idx, test_idx) in enumerate(kf.split(X), start=1):
    X_tr, X_te = X.iloc[train_idx], X.iloc[test_idx]
    y_tr, y_te = y.iloc[train_idx], y.iloc[test_idx]
    model.fit(X_tr, y_tr)
    acc = accuracy_score(y_te, model.predict(X_te))
    fold_accuracies.append(acc)
    print(f"Fold {fold} Accuracy: {acc:.4f}")

print("Average Accuracy:", np.mean(fold_accuracies).round(4))
