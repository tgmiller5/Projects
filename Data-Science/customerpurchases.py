# coding: utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

pd.set_option('max_columns', 50)
mpl.rcParams['lines.linewidth'] = 2

df = pd.read_excel('MillerFoods.xlsx')
df.head()
df['OrderPeriod'] = df.OrderDate.apply(lambda x: x.strftime('%Y-%m'))
df.head()

df.set_index('UserId', inplace=True)
df['CohortGroup'] = df.groupby(level=0)['OrderDate'].min().apply(lambda x: x.strftime('%Y-%m'))
df.reset_index(inplace=True)
df.head()
grouped = df.groupby(['CohortGroup', 'OrderPeriod'])
cohorts = grouped.agg({'UserId': pd.Series.nunique, 'OrderId': pd.Series.nunique,'TotalCharges': np.sum})
cohorts.rename(columns={'UserId': 'TotalUsers', 'OrderId': 'TotalOrders'}, inplace=True)
cohorts.head()

def cohort_period(df):
    df['CohortPeriod'] = np.arange(len(df)) +1 
    return df

cohorts = cohorts.groupby(level=0).apply(cohort_period)
cohorts.head()
x = df[(df.CohortGroup == '2013-01') & (df.OrderPeriod == '2009-01')]
y = cohorts.ix[('2013-01', '2013-01')]


x = df[(df.CohortGroup == '2013-01') & (df.OrderPeriod == '2013-09')]
x = df[(df.CohortGroup == '2013-05') & (df.OrderPeriod == '2013-09')]
y = cohorts.ix[('2013-05', '2013-09')]
print y
print x

cohorts.reset_index(inplace=True)
cohorts.set_index(['CohortGroup', 'CohortPeriod'], inplace=True)
cohort_group_size = cohorts['TotalUsers'].groupby(level=0).first()
cohort_group_size.head()
cohorts['TotalUsers'].head()
cohorts['TotalUsers'].unstack(0).head()
user_retention = cohorts['TotalUsers'].unstack(0).divide(cohort_group_size, axis=1)
user_retention.head(10)
user_retention[['2013-06', '2013-07', '2013-08']].plot(figsize=(10,5))

plt.show()
plt.title('Cohorts: User Retention')
plt.xticks(np.arange(1, 12.1, 1))
plt.xlim(1, 12)
plt.ylabel('% of Cohort Purchasing');

import seaborn as sns
sns.set(style='white')
plt.figure(figsize=(12, 8))
plt.title('Cohorts: User Retention')
sns.heatmap(user_retention.T, mask=user_retention.T.isnull(), annot=True, fmt='.0%');
plt.show()

