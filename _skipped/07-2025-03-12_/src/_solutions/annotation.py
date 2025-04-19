fig, ax = plt.subplots(figsize=(10,6))
ax.plot(X, C, color="green", label="cosine")
ax.plot(X, S, linestyle="--", linewidth=3.5, label="sine")
ax.set_title("My awesome matplotlib figure", size=16)
ax.legend(fontsize=12)
ax.set_xlim([-4,4])
ax.set_xticks([-np.pi, 0, np.pi])
ax.set_yticks([-1, 0, 1])
ax.set_xticklabels(['$-\pi$', '$0$', '$+\pi$'], size=12)
ax.grid()

# Line
ax.plot([-np.pi,np.pi],[1,1],'b--',label="Gerade")

# Point
ax.plot(np.pi/2, 1,'ro',label="Punkt")

# Annotation
_ = plt.annotate(r'$\frac{\pi}{2}$', xy=(np.pi/2, 1), xytext=(np.pi/2, 0.5),
             arrowprops=dict(facecolor='black', shrink=0.05, width=0.5, headwidth=4),
             fontsize=15, color='k')