print(gdf.shape)
# use either loc method
print(gdf.loc[:, ['longitude', 'latitude']].isnull().sum())
# or select with a list of columns
print(gdf[['longitude', 'latitude']].isnull().sum())