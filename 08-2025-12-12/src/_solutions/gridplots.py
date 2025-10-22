import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.linspace(0, 2 * np.pi, 100)
y_data = [
    np.sin(x),
    np.cos(x),
    np.tan(x),
    np.exp(-x) * np.sin(2 * x),
    np.log(x + 1),
    np.sqrt(x),
    x**3 + 4.5*np.cos(10*x),
    np.log(x**2 + 1) + 10/((x+1)**2),
    np.tanh(x)    
]

# rows, columns
nrows, ncols = 3, 3

# Subplots
fig, axs = plt.subplots(nrows, ncols, figsize=(12, 10))


for i in range(nrows):
    for j in range(ncols):
        index = i * ncols + j  # Berechne den Index für den Zugriff auf y_data
        axs[i, j].plot(x, y_data[index])
        axs[i, j].set_title(f'Plot {index + 1}')


plt.tight_layout()
plt.show()