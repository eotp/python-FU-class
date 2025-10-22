import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def sigmoid(x, x0, k):
    y = 1 / (1 + np.exp(-k*(x-x0)))
    return y

(x0, k), _ = curve_fit(sigmoid, x, y)

xnew = np.linspace(-1, 31, 50)
yfit = sigmoid(xnew, x0, k)

fig, ax = plt.subplots(figsize=(12,6))
ax.scatter(x, y, marker='o', color="r", label="data")
ax.plot(xnew, yfit, color="blue");