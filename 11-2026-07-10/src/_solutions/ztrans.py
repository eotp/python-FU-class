def ztrans(X):
    return (X - np.mean(X)) / np.std(X)

fig, ax = plt.subplots()
ax.hist(ztrans(heights), bins=25)
ax.set_xlabel('z-scores', size=16);