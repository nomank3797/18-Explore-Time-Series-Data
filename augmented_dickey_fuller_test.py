from pandas import read_csv
from statsmodels.tsa.stattools import adfuller

# load the dataset
series = read_csv('IHEPC_months.csv', header=0, index_col=0)
series = series['Global_active_power']
X = series.values
result = adfuller(X)
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
	print('\t%s: %.3f' % (key, value))
