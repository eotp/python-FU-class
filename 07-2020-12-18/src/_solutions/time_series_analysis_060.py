## Solution Challenge 6

#Solution 1
#first plot
fig, ax = plt.subplots()
data_monthly['anomaly'].plot.hist(bins = 20)

#second plot
fig, ax = plt.subplots()
cond_1 = ((data_monthly['year'] >= 1850) & (data_monthly['year'] <= 1900)) #condition 1
cond_2 = ((data_monthly['year'] >= 1950) & (data_monthly['year'] <= 2000)) #condition 2

data_monthly.loc[cond_1]['anomaly'].hist(bins=20, alpha=0.4, ax=ax)
data_monthly.loc[cond_2]['anomaly'].hist(bins=20, alpha=0.4, ax=ax)

#Solution 2
'''
fig, ax = plt.subplots()
data_monthly.anomaly.plot.hist(bins=20, ax=ax)

fig, ax = plt.subplots()
data_monthly.anomaly.loc["1850":"1900"].hist(bins=20, alpha=0.4, ax=ax)
data_monthly.anomaly.loc["1950":"2000"].hist(bins=20, alpha=0.4, ax=ax)
'''