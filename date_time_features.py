from pandas import read_csv
from pandas import DataFrame
from pandas import concat
series = read_csv('IHEPC_months.csv', header=0, parse_dates=[0], index_col=0)
series = series['Global_active_power']
temps = DataFrame(series.values)
dataframe = concat([temps.shift(1), temps], axis=1)
dataframe.columns = ['t-1', 't']
print(dataframe.head(5))

dataframe1 = concat([temps.shift(3), temps.shift(2), temps.shift(1), temps], axis=1)
dataframe1.columns = ['t-3', 't-2', 't-1', 't']
print(dataframe1.head(5))
