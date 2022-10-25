# Generate data points to be computed  
x_new = np.linspace(0,1,200)
# Fit generated data with paramters
fit_y = model_func(x_new, y0, m, C)