from scipy.constants import G # Gravitationskonstante
from scipy.constants import g # Schwerebeschleunigung
# Konstanten für die Berechnung der Erdmasse
masse_erde_kg = 5.9722e24  # Masse der Erde in Kilogramm

# Berechnung der Erdmasse
erdmasse_kg = (1/G* g )* 10**(-24)*(6378000)**2

print("Erdmasse:", erdmasse_kg, "10^(24) kg")