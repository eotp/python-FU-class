import matplotlib.pyplot as plt
import numpy as np

# Beispiel-Daten
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(-x) * np.sin(2 * x)
y5 = np.log(x + 1)
y6 = np.sqrt(x)

# Subplots: 3 rows , 2 columns
fig, axs = plt.subplots(3, 2, figsize=(10, 10))

# Plot 1: Sinus
axs[0, 0].plot(x, y1)
axs[0, 0].set_title('Sinus')

# Plot 2: Cosinus
axs[0, 1].plot(x, y2)
axs[0, 1].set_title('Cosinus')

# Plot 3: Tangens
axs[1, 0].plot(x, y3)
axs[1, 0].set_title('Tangens')

# Plot 4: Exponentialfunktion
axs[1, 1].plot(x, y4)
axs[1, 1].set_title('Exponentialfunktion')

# Plot 5: Logarithmus
axs[2, 0].plot(x, y5)
axs[2, 0].set_title('Logarithmus')

# Plot 6: Quadratwurzel
axs[2, 1].plot(x, y6)
axs[2, 1].set_title('Quadratwurzel')


plt.tight_layout()
plt.show()