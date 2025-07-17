import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Load your actual and predicted values
# Assuming 'actual.csv' and 'predicted.csv' contain the actual and predicted values respectively
# with a column named 'value'
actual_data = pd.read_csv('/content/Dataset- Superstore (2015-2018).csv')  # Replace with your path to actual data
predicted_data = pd.read_csv('/content/Dataset- Superstore (2015-2018).csv')  # Replace with your path to predicted data

# Extracting the values (adjust the column name as needed)
y_test = actual_data['Sales'].values
y_pred = predicted_data['Profit'].values

# Calculate Mean Absolute Error (MAE)
mae = mean_absolute_error(y_test, y_pred)

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)

# Calculate Mean Absolute Percentage Error (MAPE)
mape = np.mean(np.abs((y_test - y_pred) / y_test)) * 100

print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"Mean Absolute Percentage Error (MAPE): {mape}%")
