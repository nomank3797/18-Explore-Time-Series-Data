# Standardize time series data
from pandas import read_csv
from sklearn.preprocessing import StandardScaler
from math import sqrt
from matplotlib import pyplot
# load the dataset and print the first 5 rows
series = read_csv('IHEPC.csv', header=0, index_col=0)
series = series['Global_active_power']
series.hist()
pyplot.show()
# prepare data for standardization
values = series.values
values = values.reshape((len(values), 1))
# train the standardization
scaler = StandardScaler()
scaler = scaler.fit(values)
print('Mean: %f, StandardDeviation: %f' % (scaler.mean_, sqrt(scaler.var_)))
# standardization the dataset and print the first 5 rows
normalized = scaler.transform(values)
for i in range(5):
	print(normalized[i])
# inverse transform and print the first 5 rows
inversed = scaler.inverse_transform(normalized)
for i in range(5):
	print(inversed[i])
