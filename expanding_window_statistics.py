# create expanding window features
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
series = read_csv('IHEPC_months.csv', header=0, parse_dates=[0], index_col=0)
series = series['Global_active_power']
temps = DataFrame(series.values)
window = temps.expanding()
dataframe = concat([window.min(), window.mean(), window.max(), temps.shift(-1)], axis=1)
dataframe.columns = ['min', 'mean', 'max', 't']
print(dataframe.head(5))
