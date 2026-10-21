import matplotlib.pyplot as plt
import numpy as np

titles = {1:'This is the first plot',2:'This is the second plot',3:'This is the third plot',4:'This is the fourth plot',5:'This is the fifth plot',6:'This is the sixth plot'}

# Beispiel-Daten
x = np.linspace(-2 * np.pi, 2 * np.pi, 10000)
y_data = [
    np.sin(x),
    np.cos(x),
    np.cos(x)**2,
    np.sin(x)**2,
    1-np.cos(x)**2,
    1-np.sin(x)**2
]

# Anzahl der Zeilen und Spalten
nrows, ncols = 3, 2

# Erstellen von Subplots mit 3 Zeilen und 2 Spalten
fig, axs = plt.subplots(nrows, ncols, figsize=(10, 10))

# Iteriere durch die Zeilen und Spalten und erstelle die Plots
for i in range(nrows):
    for j in range(ncols):
        index = i * ncols + j  # Berechne den Index für den Zugriff auf y_data
        ax = axs[i, j]
        ax.plot(x, y_data[index])
        ax.set_title(f'{titles[index + 1]}')
        format_graph(ax)
        
# Anpassungen und Anzeige der Plots
plt.tight_layout()
plt.show()