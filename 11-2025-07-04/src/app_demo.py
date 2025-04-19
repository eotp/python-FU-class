# """ Run the file with: streamlit run [filename] """

from datetime import date
from re import M

#
import folium
import geopandas as gpd
import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
from streamlit_folium import folium_static

import utils

# """ 0. Load Datasets """
# utils.load_files() is marked with the @st.cache keyword
# Caching allows to store return variables in memory
# Saving execution time for time costly operations
(
    _europe,
    _bl,
    _kreise,
    _kreise_full,
    _gdf_europe,
    _world,
    _world_full,
) = utils.load_files()
europe = _europe.copy()
bl = _bl.copy()
kreise = _kreise.copy()
kreise_full = _kreise_full.copy()
gdf_europe = _gdf_europe.copy()
world = _world.copy()
world_full = _world_full.copy()


# # """ 1. Design the app """
# # """ 1.1 Main screen """
st.title("Powerplants")
#
st.dataframe(world[[col for col in world.columns if col != "geometry"]])
# # """ 1.2. Build sidebar """
st.sidebar.title("Data selection")
#
# # """ 1.2.1. SelectBox allowing to a specific fuel type """
fuel_type = st.sidebar.selectbox(
    "Select a fuel type",
    ["All", "Green"] + list(sorted(world_full["primary_fuel"].unique())),
)

# print(fuel_type)

# st.title(str(fuel_type))
#
# # """ 1.2.2. SelectBox allowing to chose to either display absolute numbers of powerplants or generated energy """
n_or_fuel_generation = st.sidebar.selectbox(
    "Display powerplants by number of by estimated Generation?",
    ["number", "generation"],
)
#
# # """ 1.2.3. SelectBox allowing to chose whether to display absolute numbers or relative (between 0 and 1) """
total_or_relative = st.sidebar.selectbox(
    "Display absolute or relative numbers?", ["absolute", "relative"]
)
#
# # Translate choice to represent internal data structure
trans_to_internal_structure = {
    "number": "N_fuel",
    "generation": "fuel_generation",
    "absolute": "total",
    "relative": "ratio",
}
#
target_col = (
    trans_to_internal_structure[n_or_fuel_generation]
    + "_"
    + trans_to_internal_structure[total_or_relative]
)
#
# # """ 1.2.4. SelectBox allowing to chose color distribution """
linear = st.sidebar.selectbox(
    "Linear Color scale or by quantiles?", ["quantiles", "linear"]
)
#
# # """ 1.2.5. SelectBox allowing to chose colormaps """
# # Chose which colors to represent in map
colormap = st.sidebar.selectbox(
    "Choose Colormap",
    [
        "Blues",
        "Greens",
        "Red to Blue",
        "Red to Green",
        "Spectral",
        "Pastel",
    ],
)
#
# # Translate colors to Colormap names
# # See: https://github.com/dsc/colorbrewer-python
trans_cmap = {
    "Blues": "Blues",
    "Greens": "Greens",
    "Red to Blue": "RdBu",
    "Red to Green": "RdYlGn",
    "Spectral": "Spectral",
    "Pastel": "Pastel1",
}
#
#
# # """ 1.2.6. SelectBox allowing to choose a Landkreis to inspect """
# # Will be of interest later on
kreis = st.sidebar.selectbox("Select a Landkreis", sorted(kreise.index.unique()))
#
# """ 2. First Map --- Whole World """
#
st.title("World")
#
utils.create_and_display_map(
    world,
    f"{target_col}_{fuel_type}",
    ["name", f"{target_col}_{fuel_type}"],
    "feature.properties.name",
    fuel_type,
    quantiles=linear == "quantiles",
    colormap=trans_cmap[colormap],
)
#
#
# # """ 3. Second Map --- German Bundesländer """
#
st.title("German Bundesländer")

utils.create_and_display_map(
    bl,
    f"{target_col}_{fuel_type}",
    ["name", f"{target_col}_{fuel_type}"],
    "feature.properties.name",
    fuel_type,
    quantiles=linear == "quantiles",
    center="ger",
    colormap=trans_cmap[colormap],
)
#
# # """ 4. Third Map --- German Landkreise """
#
st.title("German Landkreise")

utils.create_and_display_map(
    kreise,
    f"{target_col}_{fuel_type}",
    ["name", f"{target_col}_{fuel_type}"],
    "feature.properties.name",
    fuel_type,
    quantiles=linear == "quantiles",
    center=kreis,
    colormap=trans_cmap[colormap],
)
#
# # """ 5. Simple Bar Plot """
# # hidden behind checkbox
if st.checkbox("Plot distribution for given Kreis"):
    pd.set_option("display.float_format", lambda x: "%.3f" % x)
    fig, ax = plt.subplots()
#
    if n_or_fuel_generation == "generation":
        kreise_full.loc[kreise_full["name"] == kreis].groupby(["primary_fuel"])[
            "estimated_generation_gwh_2020"
        ].sum().plot.bar(ax=ax)
        ax.set_title(f"Generation by type of Powerplant in {kreis}")
        ax.set_ylabel("Energy Generation in GWh")

    else:
        kreise_full.loc[kreise_full["name"] == kreis].groupby(["primary_fuel"])[
            "estimated_generation_gwh_2020"
        ].size().plot.bar(ax=ax)
        ax.set_title(f"Number of Powerplants in {kreis}")
    ax.grid()
    if st.checkbox("Logarithmic Scale"):
        ax.set_yscale("log")
    st.pyplot(fig)

# # """ 6. Simple Streamlit map """"

# # hidden behind checkbox
if st.checkbox("Show Simple Map"):
    print(kreise_full.columns)
    temp_df = world_full.copy()
    if fuel_type == "Green":
        temp_df = temp_df.loc[temp_df["green"]]
    elif fuel_type != "All":
        temp_df = temp_df.loc[temp_df["primary_fuel"] == fuel_type]
    temp_df["lat"] = temp_df["latitude"]
    temp_df["lon"] = temp_df["longitude"]
    # streamlit needs latitude and logitude coordinates to be represented like this
    temp_df = temp_df[["lat", "lon"]].drop_duplicates()
    st.map(temp_df)


# # """ 7. Marker-Cluster Map (instead of Choropleth Map)"""

# hidden behind checkbox
if st.checkbox("Show Marker Cluster Map"):
    temp_df = world_full.copy()
    if fuel_type == "Green":
        temp_df = temp_df.loc[temp_df["green"]]
    elif fuel_type != "All":
        temp_df = temp_df.loc[temp_df["primary_fuel"] == fuel_type]
    folium_static(utils.markerCluster(temp_df))
