(pd.datetime.now() - df['created_at']).loc['BarackObama'].days
df.loc['BarackObama', 'tweet_count']/(pd.datetime.now() - df['created_at']).loc['BarackObama'].days

#For all users:
#pd.DataFrame(pd.datetime.now() - df['created_at'])['created_at'].dt.days