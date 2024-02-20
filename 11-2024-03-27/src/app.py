# """ Run the file with: streamlit run [filename] """

from datetime import date

import folium
import geopandas as gpd
import pandas as pd
import streamlit as st
from folium.plugins import FastMarkerCluster
from matplotlib import pyplot as plt
from streamlit_folium import folium_static

import utils

# """ 0. Load Datasets """
# utils.load_files() is marked with the @st.cache keyword
# Caching allows to store return variables in memory
# Saving execution time for time costly operations
_europe, _bl, _kreise, _kreise_full, _gdf_europe = utils.load_files()
europe = _europe.copy()
bl = _bl.copy()
kreise = _kreise.copy()
kreise_full = _kreise_full.copy()
gdf_europe = _gdf_europe.copy()


# """ Title :-) """

st.title("WW2 Airstrikes")

# Spyder, hint: Comment out multiple lines by pressing CTRL + 1
# """ 1. First Map --- Plain Map """
#
# st.title("1. Plain Map")

# plain_map = folium.Map()

# folium_static(plain_map)

# #""" 2. Centered Map """
#
# st.title("2. Centered Map")
#
# # chosen location is roughly in the center of Germany
# # zoom_start: higher -> further zoomed in
# centered_map = folium.Map(location=[50.736950, 10.285853], zoom_start=5)
#
# folium_static(centered_map)
#
# #""" 3. Take a look at the dataframe supplied """
#
# st.title("Inspecting the DataFrame")
#
# # streamlit has trouble displaying the geometry column (containing coordinates) so we simply ignore it
# st.dataframe(europe[[x for x in europe.columns if x != "geometry"]])
#
# st.write("Columns of interest for us are:")
# st.code("['name', 'attacks_year', 'explosives_weight_year']")

# st.write("For now let's use: 'name' and 'attacks_1944'")
# st.code("columns = ['name', 'attacks_1944']")

# columns = ["name", "attacks_1944"]
# #""" 4. Show some data on map """
#
# st.title("4. Show some data on Map")

# # Choropleth maps values over maps
# choropleth = folium.Choropleth(
#     geo_data=europe,  # lookup for geo locations
#     data=europe,  # lookup for actual data
#     key_on=f"feature.properties.name",  # weird stuff, "JSON Index to find datapoints with"; usually feature.properties.NAME_COLUMN
#     columns=columns,  # columns to include (usually: [NAME_COLUMN, NUMERICAL_VALUE_COLUMN])
#     name="Choropleth v1",
# )

# choropleth.add_to(centered_map)

# folium_static(centered_map)
#
# #""" 5. Extending it and exploring options """
#
# st.title("5. Extending it and exploring options")

# # quantiles to use to split color flow on data
# quantiles = [0, 0.1, 0.5, 0.75, 0.9, 0.975, 0.99, 1]

# choropleth = folium.Choropleth(
#     geo_data=europe,  # lookup for geo locations
#     data=europe,  # lookup for actual data
#     key_on="feature.properties.name",  # weird stuff, "JSON Index to find datapoints with"; usually feature.properties.NAME_COLUMN
#     columns=columns,  # columns to include (usually: [NAME_COLUMN, NUMERICAL_VALUE_COLUMN])
#     name="Choropleth v2",  # name of layer
#     fill_color="YlOrBr",  # colormap to use
#     legend_name="Number of Attacks",  # selfexplanatory
#     bins=europe[columns[1]]
#     .quantile(quantiles)
#     .tolist(),  # bins to put numerical data to (and apply colormap accordingly)
#     highlight=True,  # highlight area on mouse-over
# )

# choropleth.add_to(centered_map)

# folium.LayerControl().add_to(centered_map)

# folium_static(centered_map)
#
# #""" 6. Adding Tooltip on Mouse-Over """
#
# st.title("6. Adding Tooltip on Mouse-Over")

# style_function = "font-size: 15px; font-weight: bold"
# choropleth.geojson.add_child(
#     folium.features.GeoJsonTooltip(
#         fields=columns,  # columns to use
#         aliases=["Name: ", "Number of Attacks: "],  # Rename columns on tooltip
#         style=style_function,  # apply fontsize
#         localize=True,  # splits large numbers by comma (e.g. 10000 -> 10,000)
#     )
# )

# choropleth.add_to(centered_map)

# folium_static(centered_map)
#
# #""" 7. Allow for dynamically selecting desired column "
#
# st.title("7. Allow for dynamically selecting desired column")
#
# #""" 7.1. Build sidebar """
#
# st.sidebar.title("Data selection")
#
# #""" 7.1.1. SelectBox allowing to choose a year between 1939 and 1945 """
# st.sidebar.header("Years of Interest")
# year = st.sidebar.selectbox("Select a year", list(range(1939, 1946)))
#
#
# #""" 7.1.2. SelectBox allowing to choose a Feature to inspect """
# st.sidebar.header("Column of Interest")
# column_of_choice = st.sidebar.selectbox(
#     "Select data of interest", ["Number of Attacks", "High Explosives Weight"]
# )
# # translate selection into actual column name used in dataset
# trans_col = {
#     "Number of Attacks": "attacks",
#     "High Explosives Weight": "explosives_weight",
# }
# column = trans_col[column_of_choice]

# st.text("Our variable choices:")

# st.text("Target Column")
# st.code(column)

# st.text("Target year")
# st.code(year)

# #""" Don't worry there's a function for creating the map! """
# #""" We don't have to rewrite all stepts from above """
# utils.create_and_display_map(
#     europe, f"{column}_{year}", ["name", f"{column}_{year}"], "feature.properties.name"
# )
#
# #""" 8. More detailed maps for Germany """
#
# st.title("8. More detailed maps for Germany")

# st.header("German Bundesländer")

# utils.create_and_display_map(
#     bl, f"{column}_{year}", ["name", f"{column}_{year}"], "feature.properties.name"
# )
#
#
# #""" 8.1. SelectBox allowing to choose a Landkreis to inspect """
# st.header("German Landkreise")
# kreis = st.sidebar.selectbox("Select a Landkreis", sorted(kreise["name"].unique()))
#
# utils.create_and_display_map(
#     kreise,
#     f"{column}_{year}",
#     ["name", f"{column}_{year}"],
#     "feature.properties.name",
#     center=kreis,
# )
#
# #""" 9. Back to the roots: Simple Plot """
# Let's build a time based plot of attacks over time for selected Landkreis

# st.title("9. Back to the roots: Simple Plot!")
#
# #""" 9.1. Slidebar to choose date interval for plot """
# date_min = kreise_full["Mission Date"].min()
# slider has a problem with pandas.datetime objects, thus we have to transform it to datetime.date
# date_min = date(date_min.year, date_min.month, date_min.day)

# date_max = kreise_full["Mission Date"].max()
# date_max = date(date_max.year, date_max.month, date_max.day)
#
# # slider takes following arguments:
# # str: title
# # numerical: minimum value
# # numerical: maximum value
# # numerical/tuple: default value(s)
# choice_date_min, choice_date_max = st.sidebar.slider(
#     "Select Date", date_min, date_max, (date_min, date_max)
# )
#
# fig, ax = plt.subplots()
# kreise_full.loc[
#     (kreise_full["name"] == kreis)
#     & (kreise_full["Mission Date"] >= pd.to_datetime(choice_date_min))
#     & (kreise_full["Mission Date"] <= pd.to_datetime(choice_date_max)),
#     "Mission Date",
# ].value_counts().sort_index().plot(ax=ax)
# # value_counts -> count how many attacks happened at each date
# # sort_index -> sort dates
# ax.grid()
# ax.set_xlabel("Date")
# ax.set_ylabel("Number of Attacks")
# st.title(f"Number of Attacks on {kreis} between {choice_date_min} - {choice_date_max}")
# st.pyplot(fig)
#
# # also hidden behind: utils.timeplot(df, target_kreis, min_date, max_name)
#
# # """ 10. We can also plot simple coordinates directly with streamlit """
# for whatever reason though streamlit expects a dataframe with columns
# 'lat' and 'lon' (meaning latitude and longitude respectively)
# so we have to translate them in our dataframe

# st.title("10. A simple streamlit-map plotting coordinates")
# temp_df = kreise_full.copy()
# temp_df = temp_df.loc[temp_df["name"] == kreis]
# temp_df["lat"] = temp_df["Target Latitude"]
# temp_df["lon"] = temp_df["Target Longitude"]
# temp_df = temp_df[["lat", "lon"]].drop_duplicates()
# st.map(temp_df)
# # """ 11. Another type of map: Marker-Cluster Map"""
#
# st.title("11. Another type of map: Marker-Cluster Map")
#
# # hidden behind checkbox
# st.warning(
#     "Map hidden behind the checkbox may take a long time to load depending on your hardware!"
# )
# if st.checkbox("Show Marker Cluster Map"):
#     cluster_map = utils.initiate_map()
#     #
#     subset = gdf_europe.loc[gdf_europe["year"] == year]
#     h = folium.FeatureGroup(name="Hydroelectric")
#     h.add_child(
#         # takes a list of x and y coordinates as input
#         FastMarkerCluster(data=subset[["Target Latitude", "Target Longitude"]])
#     )
#     cluster_map.add_child(h)

#     utils.add_tiles(cluster_map)

#     folium_static(cluster_map)
#
# =============================================================================
