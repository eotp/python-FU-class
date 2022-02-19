# """ Run the file with: streamlit run [filename] """

from datetime import date

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
_europe, _bl, _kreise, _kreise_full, _gdf_europe = utils.load_files()
europe = _europe.copy()
bl = _bl.copy()
kreise = _kreise.copy()
kreise_full = _kreise_full.copy()
gdf_europe = _gdf_europe.copy()


# """ 1. Design the app """
# """ 1.1 Main screen """
st.title("WW2 Airstrikes")

# """ 1.2. Build sidebar """
st.sidebar.title("Data selection")
st.sidebar.header("Years of interest")

# """ 1.2.1. SelectBox allowing to choose a year between 1939 and 1945 """
year = st.sidebar.selectbox("Select a year", list(range(1939, 1946)))

# """ 1.2.2. SelectBox allowing to choose a Feature to inspect """
column_of_choice = st.sidebar.selectbox(
    "Select data of interest", ["Number of Attacks", "High Explosives Weight"]
)
# translate selection into actual column name used in dataset
trans_col = {
    "Number of Attacks": "attacks",
    "High Explosives Weight": "explosives_weight",
}
column = trans_col[column_of_choice]

# """ 1.2.3. SelectBox allowing to choose a Landkreis to inspect """
kreis = st.sidebar.selectbox("Select a Landkreis", sorted(kreise["name"].unique()))

# """ 1.2.4. Slidebar to choose date interval for plot """
date_min = kreise_full["Mission Date"].min()
date_min = date(date_min.year, date_min.month, date_min.day)

date_max = kreise_full["Mission Date"].max()
date_max = date(date_max.year, date_max.month, date_max.day)

y_min, y_max = st.sidebar.slider(
    "Select Date", date_min, date_max, (date_min, date_max)
)


# """ 2. First Map --- Whole Europe """

st.title("Europe")

utils.create_and_display_map(
    europe, f"{column}_{year}", ["name", f"{column}_{year}"], "feature.properties.name"
)

# """ 3. Second Map --- German Bundesländer """

st.title("German Bundesländer")

utils.create_and_display_map(
    bl, f"{column}_{year}", ["name", f"{column}_{year}"], "feature.properties.name"
)

# """ 4. Third Map --- German Landkreise """

st.title("German Landkreise")

utils.create_and_display_map(
    kreise,
    f"{column}_{year}",
    ["name", f"{column}_{year}"],
    "feature.properties.name",
    center=kreis,
)

# """ 5. Time Plot for chosen Landkreis (see 1.2.3.) """

utils.timeplot(kreise_full, kreis, y_min, y_max)
# hidden behind checkbox
if st.checkbox("Show Targets"):
    temp_df = kreise_full.copy()
    temp_df = temp_df.loc[temp_df["name"] == kreis]
    temp_df["lat"] = temp_df["Target Latitude"]
    temp_df["lon"] = temp_df["Target Longitude"]
    temp_df = temp_df[["lat", "lon"]].drop_duplicates()
    st.map(temp_df)

# """ 6. Marker-Cluster Map (instead of Choropleth Map)"""

# hidden behind checkbox
if st.checkbox("Show Marker Cluster Map"):

    folium_static(utils.markerCluster(gdf_europe.loc[gdf_europe["year"] == year]))
