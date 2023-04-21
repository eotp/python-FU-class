print(f"Most tweets in the last 7 days: {df['n_recent_tweets'].idxmax()} with {df['n_recent_tweets'].max()}")
df['n_recent_tweets'].sort_values(ascending = False)