def format_graph(ax):
    ax.set_xlim([-4,4])
    ax.set_xticks([-np.pi, 0, np.pi])
    ax.set_yticks([-1, 0, 1])
    ax.set_xticklabels(['$-\pi$', '$0$', '$+\pi$'], size=12)
    ax.grid()