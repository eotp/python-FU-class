import numpy as np

def datagen(x, m=5, c=10, seed=42):
    np.random.seed(seed)
    subset = np.random.choice(x, int(x.shape[0] * 0.8))
    noise = np.random.normal(0, 1, subset.shape)
    return np.reshape(subset, (-1,1)), np.reshape((subset + noise) * m + c, (-1,1))