import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

np.random.seed(0)
churn_data = pd.DataFrame({
    'MonthlyCharges': np.random.uniform(20, 100, 200),
    'DataUsageGB': np.random.uniform(10, 80, 200),
    'ContractYears': np.random.randint(1, 4, 200),
    'Churn': np.random.choice([0, 1], 200, p=[0.7, 0.3])
})
X = churn_data.drop('Churn', axis=1)
y = churn_data['Churn']

# 70% Train / 30% Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print("70/30 Split -> Train:", X_train.shape, "Test:", X_test.shape)

# 60% Train / 20% Validation / 20% Test Split
X_temp, X_test2, y_temp, y_test2 = train_test_split(X, y, test_size=0.2, random_state=42)
X_train2, X_val, y_train2, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42)
print("60/20/20 Split -> Train:", X_train2.shape, "Val:", X_val.shape, "Test:", X_test2.shape)
