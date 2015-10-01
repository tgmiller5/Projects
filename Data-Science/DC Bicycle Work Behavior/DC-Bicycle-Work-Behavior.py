
import pandas as pd
import numexpr as ne
import matplotlib.pyplot as plt
import seaborn; seaborn.set()
import numpy as np

#https://jakevdp.github.io/blog/2015/07/23/learning-seattles-work-habits-from-bicycle-counts/?utm_source=Python+Weekly+Newsletter&utm_campaign=bde289d72f-Python_Weekly_Issue_203_August_6_2015&utm_medium=email&utm_term=0_9e26887fc5-bde289d72f-312716593
#data is pulled from http://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset and using the hour csv file
data = pd.read_csv('hour1.csv', index_col='Date', parse_dates=True)
#print data.head()
#use data columns casual and registered from data
data.columns = ['casual', 'registered']
#anything that have na will be 0
data.fillna(0, inplace=True)

#will total data of casual and registered
data['Total'] = data.eval('casual + registered')
#data is resample to see the weekly trend in trips over near three year period
#the data shows how there is a strong spike in April-Julyy
#data.resample('W', how='sum').plot()
#plt.ylabel('weekly trips');
#plt.show()
pivoted = data.pivot_table(['casual', 'registered'], index=data.index.date, columns=data.index.hour, fill_value=0)
print pivoted.head()
X = pivoted.values
print X.shape

from sklearn.decomposition import PCA
Xpca = PCA(0.9).fit_transform(X)
print Xpca.shape

total_trips = X.sum(1)
plt.scatter(Xpca[:,0], Xpca[:, 1], c = total_trips, cmap='cubehelix')
plt.colorbar(label='total trips');
plt.show()

from sklearn.mixture import GMM
gmm = GMM(2, covariance_type='full', random_state=0)
gmm.fit(Xpca)
cluster_label = gmm.predict(Xpca)
plt.scatter(Xpca[:, 0], Xpca[:, 1], c=cluster_label);
plt.show()

pivoted['Cluster'] = cluster_label
data = data.join(pivoted['Cluster'], on=data.index.date)
print data.head()

by_hour = data.groupby(['Cluster', data.index.time]).mean()
print by_hour.head()

#start a #12 as there is an error 9/5/2015
fig, ax = plt.subplots(1, 2, figsize=(14, 5))
hourly_ticks = 4 * 60 * 60 * np.arange(6)

for i in range(2):
    by_hour.ix[i].plot(ax=ax[i], xticks=hourly_ticks)
    print ax[i].set_title('Cluster {0}'.format(i))
    print ax[i].set_ylabel('average hourly trips')

#13 dayofthe week

dayofweek = pd.to_datetime(pivoted.index).dayofweek
plt.scatter(Xpca[:, 0], Xpca[:, 1], c=dayofweek, cmap=plt.cm.get_cmap('jet', 7))
cb = plt.colorbar(ticks=range(7))
cb.set_ticklabels(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
plt.clim(-0.5, 6.5);
plt.show()
    
results = pd.DataFrame({'cluster': cluster_label,
                        'is_weekend': (dayofweek > 4),
                        'weekday': pivoted.index.map(lambda x: x.strftime('%a'))},
                       index=pivoted.index)
print results.head()

weekend_workdays = results.query('cluster == 0 and is_weekend')
print len(weekend_workdays)

midweek_holidays = results.query('cluster == 1 and not is_weekend')
print len(midweek_holidays)

from pandas.tseries.holiday import USFederalHolidayCalendar
cal = USFederalHolidayCalendar()
holidays = cal.holidays('2012', '2016', return_name=True)
print holidays.head()

holidays_all = pd.concat([holidays,
                         "Day Before " + holidays.shift(-1, 'D'),
                         "Day After " + holidays.shift(1, 'D')])
holidays_all = holidays_all.sort_index()
print holidays_all.head()

holidays_all.name = 'name'  # required for join
joined = midweek_holidays.join(holidays_all)
set(joined['name'])


set(holidays) - set(joined.name)

fridays = (dayofweek == 4)
plt.scatter(Xpca[:, 0], Xpca[:, 1], c='gray', alpha=0.2)
plt.scatter(Xpca[fridays, 0], Xpca[fridays, 1], c='yellow');
plt.show()

weird_fridays = pivoted.index[fridays & (Xpca[:, 0] < -600)]
weird_fridays

all_days = data.pivot_table('Total', index=data.index.time, columns=data.index.date)
all_days.loc[:, weird_fridays].plot();
all_days.mean(1).plot(color='gray', lw=5, alpha=0.3, xticks=hourly_ticks);
plt.show()
