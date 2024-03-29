from pandas import read_csv
from pandas import datetime
series = read_csv('IHEPC_months.csv', header=0, parse_dates=[0], index_col=0)
series = series['Global_active_power']
resample = series.resample('Q')
quarterly_mean_sales = resample.mean()
print(quarterly_mean_sales.head())
