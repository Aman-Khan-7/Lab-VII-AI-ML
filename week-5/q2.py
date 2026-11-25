import pandas as pd
import numpy as np

np.random.seed(42)
performance_scores = np.random.normal(loc=75, scale=10, size=100)
performance_scores[10] = 150
performance_scores[25] = -20
performance_scores[50] = 5

employee_df = pd.DataFrame({
    'EmployeeID': range(1, 101),
    'PerformanceScore': performance_scores.round(0)
})

Q1 = employee_df['PerformanceScore'].quantile(0.25)
Q3 = employee_df['PerformanceScore'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = employee_df[
    (employee_df['PerformanceScore'] < lower_bound) |
    (employee_df['PerformanceScore'] > upper_bound)
]
print("Detected Outliers:\n", outliers)

# Capping (Winsorization)
employee_df.loc[employee_df['PerformanceScore'] > upper_bound, 'PerformanceScore'] = upper_bound
employee_df.loc[employee_df['PerformanceScore'] < lower_bound, 'PerformanceScore'] = lower_bound

print("\nAfter capping (rows 10, 25, 50):\n", employee_df.iloc[[10, 25, 50]])
