from sklearn.datasets import fetch_california_housing

housing = fetch_california_housing(as_frame=True)
housing_df = housing.frame

chosen_cols = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population']
selected_features_df = housing_df[chosen_cols]

print("First 5 rows:\n", selected_features_df.head())
print("\nSelected columns:\n", selected_features_df.columns)
# Reducing features simplifies the model, speeds up training, and reduces overfitting.
