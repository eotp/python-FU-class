import folium
import geopandas as gpd
import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
from streamlit_folium import folium_static


# Caching allows to store return variables in memory
# Saving execution time for time costly operations
@st.cache
def load_files():
    """
    Loads necessary files and transforms them (in case they already shouldn't be in) to
        CRS::EPSG:4326
    """
    europe = pd.read_pickle("../data/europe_attacks.p").to_crs("EPSG:4326")
    bl = pd.read_pickle("../data/bl_attacks.p").to_crs("EPSG:4326")
    kreise = pd.read_pickle("../data/kreise_attacks.p").to_crs("EPSG:4326")
    kreise_full = pd.read_pickle("../data/kreise_full.p").to_crs("EPSG:4326")
    gdf_europe = pd.read_pickle("../data/gdf_europe.p").to_crs("EPSG:4326")
    return europe, bl, kreise, kreise_full, gdf_europe


def initiate_map(location=[50.736950, 10.285853], zoom_start=5):
    # create and centralize map around specified coordinates
    map = folium.Map(location=location, zoom_start=zoom_start)

    return map


def add_tiles(map):

    # allow for map-flavour selection
    tiles = ["stamenwatercolor", "cartodbpositron", "openstreetmap", "stamenterrain"]
    for tile in tiles:
        folium.TileLayer(tile).add_to(map)

    folium.LayerControl().add_to(map)


def create_choropleth(data, column, columns, key_on):
    """
    Create Choropleth (see: https://python-visualization.github.io/folium/quickstart.html#Choropleth-maps)
    for passed dataset.

    Basically an overlay map displaying numerical values over geographic areas
    """

    # potential quantiles to include
    # colormap will be a stepwise change from yellow to brown
    # only choose quantiles with values changing inbetween for colorstep

    pot_quantiles = [0, 0.025, 0.1, 0.25, 0.5, 0.75, 0.9, 0.975, 0.99, 1]
    quantiles = data[column].quantile(pot_quantiles).diff() == 0
    quantiles = quantiles.loc[~quantiles].index.to_list()
    if len(quantiles) < 4:
        # Colormap needs 4 bins
        quantiles = [0, 0.99, 0.99, 1]

    # actual choropleth

    choropleth = folium.Choropleth(
        geo_data=data,  # geodata
        data=data,  # numerical data
        key_on=key_on,  # weird stuff, "JSON Index to find datapoints with"; usually feature.properties.NAME_COLUMN
        columns=columns,  # columns to include (usually: [NAME_COLUMN, NUMERICAL_VALUE_COLUMN])
        fill_color="YlOrBr",  # colormap to use
        legend_name='Number of Attacks',  # selfexplanatory
        bins=data[column]
        .quantile(quantiles)
        .tolist(),  # bins to put numerical data to (and apply colormap accordingly)
        highlight=True,  # highlight area on mouse-over
        name="Choropleth"  # name of Layer
    )

    style_function = "font-size: 15px; font-weight: bold"
    if "explosives_weight" in column:
        choropleth.geojson.add_child(
            folium.features.GeoJsonTooltip(
                fields=[str(x) for x in columns],
                aliases=["Name: ", "High Explosives Weight (Tons): "],
                style=style_function,
                localize=True,
            )
        )
    else:
        choropleth.geojson.add_child(
            folium.features.GeoJsonTooltip(
                fields=[str(x) for x in columns],
                aliases=["Name: ", "Number of Attacks: "],
                style=style_function,
                localize=True,
            )
        )

    return choropleth


def create_and_display_map(data, column, columns, key_on, center=None):
    if center is not None:
        # Center map around chosen location (Landkreis)
        location = data.loc[data["name"] == center].centroid
        location = [location.y, location.x]
        zoom_start = 8
    else:
        location = [50.736950, 10.285853]
        zoom_start = 5
    map = initiate_map(location=location, zoom_start=zoom_start)

    create_choropleth(data, column, columns, key_on).add_to(map)

    add_tiles(map)

    folium_static(map)


def timeplot(df, target_name, min_date, max_date):
    """
    Create time based plot. In this case number of attacks accross chosen dates
    """
    fig, ax = plt.subplots()
    df.loc[
        (df["name"] == target_name)
        & (df["Mission Date"] >= pd.to_datetime(min_date))
        & (df["Mission Date"] <= pd.to_datetime(max_date)),
        "Mission Date",
    ].value_counts().sort_index().plot(ax=ax)
    ax.grid()
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of Attacks")
    st.title(f"Number of Attacks on {target_name} between {min_date} - {max_date}")
    st.pyplot(fig)

def markerCluster(df):
    """
    Create a Map with Clusters of Markers
    """
    from folium import IFrame
    from folium.plugins import MarkerCluster

    cluster_map = initiate_map()

    h = folium.FeatureGroup(name="Hydroelectric")
    h.add_child(
        # takes a list of x and y coordinates as input
        MarkerCluster(
            locations=list(zip(df["Target Latitude"], df["Target Longitude"]))
        )
    )
    cluster_map.add_child(h)

    add_tiles(cluster_map)

    return cluster_map
