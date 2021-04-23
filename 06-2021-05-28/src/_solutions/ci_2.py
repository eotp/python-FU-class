from scipy.stats import t
alpha = 0.05
lower_t = t.ppf(alpha/2, df=chicken.shape[0]-1)
upper_t = t.ppf(1-alpha/2, df=chicken.shape[0]-1)
print(lower_t, upper_t)

t_ = abs(lower_t) 
t_