gdf.loc[gdf["primary_fuel"].isin(green_fuels)]

# Check selection
gdf.loc[gdf['green'] == True]==gdf.loc[gdf["primary_fuel"].isin(green_fuels)]