g = sns.FacetGrid(data=iris, col="species", hue = "species")
g.map(plt.scatter, "sepal_length", "sepal_width", alpha=.7);