!pip install pmdarima
import pmdarima

from pmdarima import auto_arima
auto_arima(train, test='adf',seasonal=True, trace=True, error_action='ignore', suppress_warnings=True)
auto_arima(y,test='adf',       # use adftest to find optimal 'd'
                       # maximum p and q
                                 # frequency of series
                       # let model determine 'd'
                      seasonal=True,   # No Seasonality


                      trace=True,
                      error_action='ignore',
                      suppress_warnings=True,
                      stepwise=True)
from statsmodels.tsa.arima.model import ARIMA
model=ARIMA(train, order=(1,1,1)).fit()
model.summary()

