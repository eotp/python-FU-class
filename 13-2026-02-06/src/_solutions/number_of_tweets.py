# Build a dictionary containing ("User": "number_of_tweets") pairs
n_recent_tweets = {}

for user in twitter_data['tweets'].keys():
    if 'data' in twitter_data['tweets'][user].keys():
        n_recent_tweets[user] = len(twitter_data['tweets'][user]['data'])
    else:
        # Lady Gaga seems to be inactive for at least the last 7 days
        n_recent_tweets[user] = 0

# our dictionary makes it simple to put our fresh extracted data into our DataFrame
# Since the DataFrame Index and the dictionary keys fit
df['n_recent_tweets'] = pd.Series(n_recent_tweets)
df