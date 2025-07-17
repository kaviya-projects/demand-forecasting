import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error
from statsmodels.tsa.arima.model import ARIMA
import warnings
import matplotlib.pyplot as plt

warnings.filterwarnings("ignore")

# Load the data
data = pd.read_csv('/content/Dataset- Superstore (2015-2018).csv', parse_dates=['Order Date'], index_col='Order Date')

# Aggregate data by month and sum up sales
monthly_sales = data['Sales'].resample('M').sum()

# Split the data into train and test sets
train_data = monthly_sales[:'2016']
test_data = monthly_sales['2017':]

# Fit the ARIMA model
arima_model = ARIMA(train_data, order=(5,1,0))  # Adjust the order (p,d,q) as needed
arima_fit = arima_model.fit()

# Make predictions
arima_pred = arima_fit.forecast(steps=len(test_data))

# Calculate accuracy metrics
mae = mean_absolute_error(test_data, arima_pred)
mse = mean_squared_error(test_data, arima_pred)
mape = np.mean(np.abs((test_data - arima_pred) / test_data)) * 100

print("ARIMA Model Predictions:")
print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"Mean Absolute Percentage Error (MAPE): {mape}%")

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(train_data, label='Train')
plt.plot(test_data, label='Test')
plt.plot(test_data.index, arima_pred, label='ARIMA Predictions', color='green')
plt.legend(loc='best')
plt.title('Sales Forecast using ARIMA')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()
