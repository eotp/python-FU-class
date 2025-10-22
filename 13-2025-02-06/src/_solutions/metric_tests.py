df['reply_count_max'] = pd.Series(tweets_metric_eval('reply_count', np.max))
df['like_count_min'] = pd.Series(tweets_metric_eval('like_count', np.min))
df['retweets_max'] = pd.Series(tweets_metric_eval('retweet_count', np.max))
df['like_count_std'] = pd.Series(tweets_metric_eval('like_count', np.std))