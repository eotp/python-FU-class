# show relative ratios in percent
((pp.isnull().sum() / pp.shape[0]) * 100).round(2)