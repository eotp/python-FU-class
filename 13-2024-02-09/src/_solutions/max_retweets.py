print(f"Most retweets on a tweet: {df['retweets_max'].idxmax()} with {df['retweets_max'].max()}")
df['retweets_max'].sort_values(ascending = False)