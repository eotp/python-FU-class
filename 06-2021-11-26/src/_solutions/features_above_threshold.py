## solution challenge 
def features_above_threshold(df, threshold=0.5):    
    n_samples = df.shape[0]
    cols2keep = df.notnull().sum()/n_samples > threshold 
    cols2keep = cols2keep.loc[cols2keep == True].index
    return cols2keep