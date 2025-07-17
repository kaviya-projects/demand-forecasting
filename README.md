# 📈 Enhancing Supermarket Inventory Management Through ARIMA and SARIMAX-Based Demand Forecasting

## 🧾 Abstract

This project employs time series analysis using the **AutoRegressive Integrated Moving Average (ARIMA)** and its seasonal variant, **Seasonal AutoRegressive Integrated Moving Average with Exogenous Variables (SARIMAX)**, to forecast retail demand across various commodities.

We utilize a dataset containing supermarket sales data from **2015 to 2018** to predict future demand. Accurate forecasting plays a vital role in inventory management and strategic decision-making in the retail sector.

By incorporating **seasonality** and **external variables**, the SARIMAX model enhances the detection of complex trends and patterns in time series data. Forecast accuracy is validated using **Mean Squared Error (MSE)** and **time series cross-validation**.

Our model enables retail businesses to make data-driven decisions, optimize inventory levels, and reduce the risks associated with overstocking or stockouts.

## 📊 Output

<img width="743" height="426" alt="Demand Forecasting Plot" src="https://github.com/user-attachments/assets/2eda6e79-a536-4c28-8558-2874895e67e8" />

## 🛠️ Technologies & Tools Used

- Python
- Pandas, NumPy
- Statsmodels (ARIMA, SARIMAX)
- Matplotlib, Seaborn
- Scikit-learn (for evaluation metrics)
- Jupyter Notebook / Google Colab

## 🔍 Key Features

- ✅ Demand forecasting for multiple retail products  
- ✅ Incorporation of seasonal trends and external factors (SARIMAX)  
- ✅ Model evaluation using **Mean Squared Error (MSE)** and **Time Series Cross-Validation**  
- ✅ Visual representation of historical and forecasted demand

## 📁 Dataset

- **Source:** Supermarket sales data (2015–2018)
- **Content:** Daily/weekly sales data for various product categories
- **Attributes:** Date, Product Name/ID, Sales Volume, Price, etc.

> The dataset used is preprocessed to remove null values, handle outliers, and aggregate sales on a time-series basis.

## 📈 Forecasting Models

### 🔹 ARIMA (AutoRegressive Integrated Moving Average)
- Captures trends and autocorrelations in the time series.
- Best for non-seasonal univariate forecasting.

### 🔹 SARIMAX (Seasonal ARIMA with Exogenous Variables)
- Handles **seasonal patterns** effectively.
- Integrates **external variables** like promotions, holidays, etc., for better accuracy.

## 📉 Evaluation Metrics

- **Mean Squared Error (MSE)**: Measures the average squared difference between actual and predicted values.
- **Time Series Cross-Validation**: Ensures reliable performance assessment by validating on sequential data splits.


## 📌 Keywords

> _Time Series Cross-Validation, ARIMA Model, SARIMAX Model, Mean Squared Error, Inventory Management, Seasonal Trends, Demand Forecasting, Supply Chain Optimization, Exogenous Variables, Retail Analytics, Forecast Accuracy._

## 💼 Applications

- Retail inventory optimization
- Supply chain planning
- Business strategy formulation
- Sales trend analysis
