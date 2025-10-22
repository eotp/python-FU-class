import matplotlib.pyplot as plt
import numpy as np

# data
x = np.linspace(-2 * np.pi, 2 * np.pi, 10000)
y_data = [
    np.sin(x),
    np.cos(x),
    x**2,
    np.exp(x),
    1-np.cos(x)**2,
    1-np.sin(x)**2
]


nrows, ncols = 2, 3


fig, axs = plt.subplots(nrows, ncols, figsize=(15, 5))


for i in range(nrows):
    for j in range(ncols):
        index = i * ncols + j
        ax = axs[i, j]
        ax.plot(x, y_data[index])
        ax.set_title(f'{titles[index + 1]}')

plt.tight_layout()
plt.show()