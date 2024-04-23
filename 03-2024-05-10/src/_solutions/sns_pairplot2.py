g = sns.FacetGrid(data=iris, col="species")
g.map(plt.scatter, "sepal_length", "sepal_width", alpha=.7);