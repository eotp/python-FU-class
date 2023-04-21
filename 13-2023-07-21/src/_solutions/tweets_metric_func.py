def tweets_metric_eval(metric, func):
    dict_metric = {}
    for user in twitter_data['tweets'].keys():
        val_list = []
        if 'data' in twitter_data['tweets'][user]:
            for tweet in twitter_data['tweets'][user]['data']:
                val_list.append(tweet['public_metrics'][metric])
        try:
            dict_metric[user] = func(val_list)
        except Exception as e:
            dict_metric[user] = np.nan
    return dict_metric