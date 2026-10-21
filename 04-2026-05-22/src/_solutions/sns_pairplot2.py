g = sns.FacetGrid(data=iris, col="species", hue = "species", height=10, aspect=0.8)
g.map(plt.scatter, "sepal_length", "sepal_width", alpha=.7);