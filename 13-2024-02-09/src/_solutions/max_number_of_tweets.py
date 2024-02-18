# Build a dictionary containing ("User": "maximum likes on tweets") pairs
most_likes = {}

for user in twitter_data['tweets'].keys():
    maxx = 0
    if 'data' in twitter_data['tweets'][user]:
        for i in range(len(twitter_data['tweets'][user]['data'])):
            maxx = max(maxx, twitter_data['tweets'][user]['data'][i]['public_metrics']['like_count'])
    most_likes[user] = maxx
    
# our dictionary makes it simple to put our fresh extracted data into our DataFrame
# Since the DataFrame Index and the dictionary keys fit
df['most_likes'] = pd.Series(most_likes)
df