print(gdf.shape)
# subset only vaild spatial coordinates
gdf = gdf.loc[gdf[['longitude', 'latitude']].notnull().all(axis = 1)]
print(gdf.shape)
gdf[['longitude', 'latitude']].isnull().sum()