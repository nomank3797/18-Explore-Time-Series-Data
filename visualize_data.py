from pandas import read_csv
from matplotlib import pyplot
from pandas import DataFrame
from pandas import Grouper
from pandas import concat
from pandas.plotting import lag_plot
from pandas.plotting import autocorrelation_plot

# load the dataset
series = read_csv('IHEPC_months.csv', header=0, parse_dates=[0], index_col=0)
series = series['Global_active_power']
print(series.head())

# Time Series Line Plot
series.plot()
pyplot.show()
series.plot(style='k.')
pyplot.show()

'''
groups = series.groupby(Grouper(freq='A'))
years = DataFrame()
for name, group in groups:
	print(name)
	years[name.year] = group.values
years.plot(subplots=True, legend=False)
pyplot.show()
'''
# Time Series Histogram
series.hist()
pyplot.show()

# Density Plots
series.plot(kind='kde')
pyplot.show()

# Time Series Box and Whisker Plots by Interval
one_year = series['2007']
groups = one_year.groupby(Grouper(freq='M'))
months = concat([DataFrame(x[1].values) for x in groups], axis=1)
months = DataFrame(months)
months.columns = range(1,13)
months.boxplot()
pyplot.show()

# Time Series Heat Maps
one_year = series['2007']
groups = one_year.groupby(Grouper(freq='M'))
months = concat([DataFrame(x[1].values) for x in groups], axis=1)
months = DataFrame(months)
months.columns = range(1,13)
pyplot.matshow(months, interpolation=None, aspect='auto')
pyplot.show()

# Time Series Lag Scatter Plots
lag_plot(series)
pyplot.show()

values = DataFrame(series.values)
lags = 8
columns = [values]
for i in range(1,(lags + 1)):
	columns.append(values.shift(i))
dataframe = concat(columns, axis=1)
columns = ['t+1']
for i in range(1,(lags + 1)):
	columns.append('t-' + str(i))
dataframe.columns = columns
pyplot.figure(1)
for i in range(1,(lags + 1)):
	ax = pyplot.subplot(240 + i)
	ax.set_title('t+1 vs t-' + str(i))
	pyplot.scatter(x=dataframe['t+1'].values, y=dataframe['t-'+str(i)].values)
pyplot.show()

# Time Series Autocorrelation Plots
autocorrelation_plot(series)
pyplot.show()
