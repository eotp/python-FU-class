auc1 = norm.cdf(mu+1*sigma, loc=mu, scale=sigma) - norm.cdf(mu-1*sigma, loc=mu, scale=sigma)
auc2 = norm.cdf(mu+2*sigma, loc=mu, scale=sigma) - norm.cdf(mu-2*sigma, loc=mu, scale=sigma)
auc3 = norm.cdf(mu+3*sigma, loc=mu, scale=sigma) - norm.cdf(mu-3*sigma, loc=mu, scale=sigma)
print(auc1, auc2, auc3)