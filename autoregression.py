from pandas import read_csv
from matplotlib import pyplot
from pandas.plotting import lag_plot
from pandas import DataFrame
from pandas import concat
from pandas.plotting import autocorrelation_plot
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.ar_model import AutoReg
from sklearn.metrics import mean_squared_error
from math import sqrt

# load the dataset
series = read_csv('IHEPC_months.csv', header=0, index_col=0)
series = series['Global_active_power']
print(series.head())
series.plot()
pyplot.show()
lag_plot(series)
pyplot.show()

values = DataFrame(series.values)
dataframe = concat([values.shift(1), values], axis=1)
dataframe.columns = ['t-1', 't+1']
result = dataframe.corr()
print(result)

autocorrelation_plot(series)
pyplot.show()

plot_acf(series, lags=31)
pyplot.show()

X = series.values
train, test = X[1:len(X)-14], X[len(X)-14:]
# train autoregression
window = 10
model = AutoReg(train, lags=10)
model_fit = model.fit()
coef = model_fit.params
# walk forward over time steps in test
history = train[len(train)-window:]
history = [history[i] for i in range(len(history))]
predictions = list()
for t in range(len(test)):
	length = len(history)
	lag = [history[i] for i in range(length-window,length)]
	yhat = coef[0]
	for d in range(window):
		yhat += coef[d+1] * lag[window-d-1]
	obs = test[t]
	predictions.append(yhat)
	history.append(obs)
	print('predicted=%f, expected=%f' % (yhat, obs))

rmse = sqrt(mean_squared_error(test, predictions))
mse = mean_squared_error(test, predictions)
print('Test RMSE: %.3f' % rmse)
print('Test MSE: %.3f' % mse)

# plot
pyplot.plot(test)
pyplot.plot(predictions, color='red')
pyplot.show()
