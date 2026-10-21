print(f"Most likes on a tweet: {df['most_likes'].idxmax()} with {df['most_likes'].max()}")
df['most_likes'].sort_values(ascending = False)