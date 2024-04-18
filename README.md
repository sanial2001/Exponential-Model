# Exponential-Model
EDA and hyperparameter tuning for exponential smoothing

- ADF-TEST :
  the ADF test provides a valuable tool for assessing the stationarity of time series data, which is essential for making reliable inferences and forecasts in various fields. The general rule of thumb being that p-value has to be less than 0.05 in order to reject null hypothesis and assume the data is stationary

- HYPERPARAMTER TUNING FOR MODEL :
  We perform hyper-parameter tuning on seasonal, trend and initialization data. The best parameters gets selected on the basis of least mse

- HYPERPARAMETER TUNING FOR MODEL.FIT() :
  We iterate over different values of alpha, beta and gamma separately ranging from 0.1 to 1 at a gradient of 0.1. Alpha is used for determining the smoothing_level, beta is used for determining the smoothing_trend and gamma is used for determining the smoothing_seasonal

