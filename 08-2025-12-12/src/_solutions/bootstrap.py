import numpy as np
import pandas as pd

def bootstrap(df, var, n_bootstrap, alpha=0.05):
    data = df.loc[:, var].reset_index(drop=True).dropna()
    n_sample = data.shape[0]   
    
    mean_statistic = []
    for b in range(n_bootstrap):
        idx = np.random.randint(low=data.index.min(), 
                                high=data.index.max()+1, 
                                size=data.shape[0])
        
        sample_mean = data.loc[idx].mean()
        mean_statistic.append(sample_mean)

        
    ordered = np.sort(mean_statistic)    
    lower, upper = np.quantile(ordered, [alpha/2, 1-alpha/2])
    mean = np.mean(ordered)
    
    return lower, mean, upper
