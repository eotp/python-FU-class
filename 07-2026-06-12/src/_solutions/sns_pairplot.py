g = sns.pairplot(iris, hue="species", plot_kws={"alpha":0.75})
g.fig.set_dpi(300)