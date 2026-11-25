import pandas as pd

# Load Kaggle Titanic dataset (train.csv)
df = pd.read_csv('train.csv')
print("Missing values before cleaning:\n", df.isnull().sum())

# Strategy 1 (Removal): Drop 'Cabin'
df = df.drop(columns=['Cabin'])

# Strategy 2 (Imputation - Median): Fill 'Age' with median
# Median is preferred over mean because age can have outliers/skewed values.
df['Age'] = df['Age'].fillna(df['Age'].median())

# Strategy 3 (Imputation - Mode): Fill 'Embarked' with mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

print("\nMissing values after cleaning:\n", df.isnull().sum())
