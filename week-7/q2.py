import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

temp = np.array([10, 15, 20, 25, 30, 12, 18, 23, 28, 32]).reshape(-1, 1)
kwh = np.array([50, 60, 75, 90, 105, 55, 70, 85, 95, 110])

X_train_elec, X_test_elec, y_train_elec, y_test_elec = train_test_split(
    temp, kwh, test_size=0.3, random_state=42
)

model = LinearRegression()
model.fit(X_train_elec, y_train_elec)

y_pred_elec = model.predict(X_test_elec)
print("Mean Squared Error (MSE):", mean_squared_error(y_test_elec, y_pred_elec))

plt.scatter(X_train_elec, y_train_elec, color='blue', label='Training Data')
plt.plot(X_train_elec, model.predict(X_train_elec), color='red', label='Regression Line')
plt.title("Temperature vs Electricity Consumption")
plt.xlabel("Temperature (C)")
plt.ylabel("Electricity (kWh)")
plt.legend()
plt.show()
