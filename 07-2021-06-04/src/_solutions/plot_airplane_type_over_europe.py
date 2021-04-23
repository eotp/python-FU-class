def plot_airplane_type_over_europe(gdf, airplane="B17", 
                                   years=[1940, 1941 ,1942, 1943, 1944, 1945], 
                                   kdp=False, aoi=europe):
    fig = plt.figure(figsize=(16,12))
    for e, y in enumerate(years):
        _gdf = gdf.loc[(gdf["year"]==y) & (gdf["Aircraft Series"]==airplane)].copy()
        _gdf.Country.replace(np.nan, "unknown", inplace=True)
        ax = fig.add_subplot(3,2,e+1)
        ax.set_aspect('equal')
        aoi.plot(ax=ax, facecolor='lightgray', edgecolor="white")
        if _gdf.shape[0] > 2:
            if kdp:
                sns.kdeplot(_gdf['Target Longitude'], _gdf['Target Latitude'], 
                            cmap="viridis", shade=True, shade_lowest=False, bw=0.25, ax=ax)   
            else:
                _gdf.plot(ax=ax, marker='o', cmap='Set1', categorical=True,
                          column='Country', legend=True, markersize=5, alpha=1)
        ax.set_title("Year: " + str(y), size=16)
    plt.tight_layout()
    plt.suptitle("Attacks of airplane {} for different years".format(airplane), size=22)
    plt.subplots_adjust(top=0.92)
    return fig, ax
    