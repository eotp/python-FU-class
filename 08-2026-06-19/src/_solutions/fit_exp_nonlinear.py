from scipy.optimize import curve_fit
def fit_exp_nonlinear(x, y):
    opt_parms, _ = curve_fit(model_func, x, y)
    y0, m, C = opt_parms
    return y0, m, C 