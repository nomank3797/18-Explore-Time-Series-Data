# Normalize time series data
from pandas import read_csv
from sklearn.preprocessing import MinMaxScaler
# load the dataset and print the first 5 rows
series = read_csv('IHEPC.csv', header=0, index_col=0)
series = series['Global_active_power']
print(series.head())
# prepare data for normalization
values = series.values
values = values.reshape((len(values), 1))
# train the normalization
scaler = MinMaxScaler(feature_range=(0, 1))
scaler = scaler.fit(values)
print('Min: %f, Max: %f' % (scaler.data_min_, scaler.data_max_))
# normalize the dataset and print the first 5 rows
normalized = scaler.transform(values)
for i in range(5):
	print(normalized[i])
# inverse transform and print the first 5 rows
inversed = scaler.inverse_transform(normalized)
for i in range(5):
	print(inversed[i])
