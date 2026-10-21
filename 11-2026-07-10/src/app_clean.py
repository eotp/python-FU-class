# """ Run the file with: streamlit run [filename] """

from datetime import date
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
_europe, _bl, _kreise, _kreise_full, _gdf_europe, _world, _world_full = utils.load_files()
europe = _europe.copy()
bl = _bl.copy()
kreise = _kreise.copy()
kreise_full = _kreise_full.copy()
gdf_europe = _gdf_europe.copy()
world = _world.copy()
world_full = _world_full.copy()


# """ 1. Design the app """
# """ 1.1 Main screen """
st.title("Powerplants")

# """ 1.2. Build sidebar """
st.sidebar.title("Data selection")
st.sidebar.header("Country of Interest")

# """ 1.2.1. SelectBox allowing to choose a year between 1939 and 1945 """
fuel_type = st.sidebar.selectbox("Select a fuel type", world_full["primary_fuel"].unique())

# """ 1.2.2. SelectBox allowing to choose a Feature to inspect """
column_of_choice = st.sidebar.selectbox(
    "Select data of interest", ["Green Energy", "Non-Green Energy"]
)
# translate selection into actual column name used in dataset
trans_col = {
    "Green Energy": "green",
    "Non-Green Energy": "ungreen",
}
column = trans_col[column_of_choice]

# """ 1.2.3. SelectBox allowing to choose a Landkreis to inspect """
kreis = st.sidebar.selectbox("Select a Landkreis", sorted(kreise.index.unique()))

# """ 2. First Map --- Whole Europe """

st.title("Europe")

utils.create_and_display_map(
    world, f"N_fuel_{fuel_type}", ["name", f"N_fuel_{fuel_type}"], "feature.properties.name", fuel_type
)

# """ 3. Second Map --- German Bundesländer """

st.title("German Bundesländer")

utils.create_and_display_map(
    bl, f"N_fuel_{fuel_type}", ["name", f"N_fuel_{fuel_type}"], "feature.properties.name", fuel_type
)

# """ 4. Third Map --- German Landkreise """

st.title("German Landkreise")

utils.create_and_display_map(
    kreise, 
    f"N_fuel_{fuel_type}", 
    ["name", f"N_fuel_{fuel_type}"], 
    "feature.properties.name", 
    fuel_type,
    center=kreis,
)

# """ 5. Time Plot for chosen Landkreis (see 1.2.3.) """

# hidden behind checkbox
if st.checkbox("Show Targets"):
    print(kreise_full.columns)
    temp_df = kreise_full.copy()
    temp_df = temp_df.loc[temp_df["name"] == kreis]
    temp_df["lat"] = temp_df["latitude"]
    temp_df["lon"] = temp_df["longitude"]
    temp_df = temp_df[["lat", "lon"]].drop_duplicates()
    st.map(temp_df)

# """ 6. Marker-Cluster Map (instead of Choropleth Map)"""

# hidden behind checkbox
if st.checkbox("Show Marker Cluster Map"):

    folium_static(utils.markerCluster(world_full))
