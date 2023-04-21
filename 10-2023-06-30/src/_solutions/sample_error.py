for n in (3, 30, 300, 3000):
    x = norm.rvs(loc=mu, scale=sigma, size=n)
    xbar = np.mean(x)
    print(f'Sampling error for n={n}: {abs(xbar-mu)}')