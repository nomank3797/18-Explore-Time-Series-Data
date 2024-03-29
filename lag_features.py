# create date time features of a dataset
from pandas import read_csv
from pandas import DataFrame
series = read_csv('IHEPC_months.csv', header=0, parse_dates=[0], index_col=0)
series = series['Global_active_power']
dataframe = DataFrame()
dataframe['year'] = [series.index[i].year for i in range(len(series))]
dataframe['month'] = [series.index[i].month for i in range(len(series))]
dataframe['Global_active_power'] = [series[i] for i in range(len(series))]
print(dataframe.head(5))
