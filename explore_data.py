# Load birth data using read_csv
from pandas import read_csv
from matplotlib import pyplot

series = read_csv('IHEPC.csv', header=0, parse_dates=[0], index_col=0)
series = series['Global_active_power']
print(type(series))

# Peek at the data
print(series.head(2))
print(series.tail(2))

# Number of observations
print(series.size)

# Querying by time
print(series['2008'])

# Descriptive statistics
print(series.describe())

# Plotting time series
pyplot.plot(series)
pyplot.show()
