import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import linkage

np.random.seed(42)
X_students = pd.DataFrame({
    'Study_Hours_Week': np.random.randint(5, 40, 50),
    'Sleep_Hours_Night': np.random.uniform(4, 9, 50).round(1)
})
X_students.loc[X_students['Study_Hours_Week'] > 30, 'Sleep_Hours_Night'] = np.random.uniform(
    4, 6, sum(X_students['Study_Hours_Week'] > 30)
).round(1)
X_students.loc[X_students['Study_Hours_Week'] < 10, 'Sleep_Hours_Night'] = np.random.uniform(
    7, 9, sum(X_students['Study_Hours_Week'] < 10)
).round(1)

Z = linkage(X_students, method='ward')
print("Linkage matrix shape:", Z.shape)
print("First 5 merges:\n", Z[:5])
