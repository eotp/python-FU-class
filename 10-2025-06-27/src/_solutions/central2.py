cases = [10,100,500,1000,5000,10000]
for case in cases:
    mu_xs = []
    for i in range(case):
        x = expon.rvs(size=n, loc=0, scale=lambda_)
        xbar = np.mean(x)
        mu_xs.append(xbar)
    sns.histplot(mu_xs, kde=True)
    print(f'True lambda: {lambda_}, mean of the sampling distribution: {np.mean(mu_xs)}')