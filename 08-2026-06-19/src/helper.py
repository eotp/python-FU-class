import cartopy.crs as ccrs
import cartopy.feature as cfeature
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

def cuteplot(
    gpd_df, 
    crs = "PlateCarree", 
    title = None, 
    kdp = False, 
    map_extent = (-27, 45, 33, 73.5), 
    color = 'red', 
    markersize = 5, 
    alpha = 0.1, 
    bw = 0.1,
    ax = None,
    label = None,
    draw_water = False
):
    """
    Function to leverage the cartopy library to plot geographical data.
    
    Parameters
    ----------
    gpd_df : geopandas.DataFrame
        DataFrame containing geographic data to be plotted
    
    crs: str, default: PlateCarree 
        Coordinate Reference System to use 
        (transforms long/lat coordinates to different x-y topologies)
        
    title: str, default: None
        Title to be set on Plot.
        
    kpd: bool, default: False
        Whether to plot a Kernel-Density Plot 
        WARNING: only works together with crs="PlateCarree"
        
    map_extent: tuple: (float, float, float, float), default: (-27, 45, 33, 73.5) (europe polygon)
        Specify plot boundaries with respect to: 
        (longitude-min, longitude-max, latitude-min, latitude-max)
        
    color: str, default: "red"
        Specify color for each plotted marker
        
    markersize: float, default: 5
        Size of each plotted marker
        
    alpha: float, default: 0.1
        Transparency value between 0 and 1
        
    bw: float, default: 0.1
        Smoothing parameter for Kernel Density Plot
        
    ax: pyplot.Axes, default: None
        You may use an existing Axes object to plot over
        
    label: str, default: None
        Label to use to produce legend
    """
    # map projections
    proj = {"PlateCarree": ("+proj=eqc +lat_ts=0 +lat_0=0 +lon_0=0 +x_0=0 +y_0=0 +ellps=WGS84 +datum=WGS84 +units=m +no_defs",
                            ccrs.PlateCarree()),
            "Mollweide": ("+proj=moll +lon_0=0 +x_0=0 +y_0=0 +ellps=WGS84 +datum=WGS84 +units=m +no_defs",
                          ccrs.Mollweide()),
            "Robinson": ("+proj=robin +lon_0=0 +x_0=0 +y_0=0 +ellps=WGS84 +datum=WGS84 +units=m +no_defs",
                         ccrs.Robinson()),
            "UTM32N": ("+proj=utm +zone=32 +ellps=intl +units=m +no_defs",
                       ccrs.EuroPP()),
            "Orthographic": ("+proj=ortho", ccrs.Orthographic())
            }

    # plot figure
    if ax is None:
        fig = plt.figure()
        ax = plt.axes(projection=proj.get(crs)[1])
        ax.stock_img()
        # add features
        if draw_water:
            ax.add_feature(cfeature.LAKES.with_scale("10m"))
            ax.add_feature(cfeature.RIVERS.with_scale("10m"))
        ax.add_feature(cfeature.LAND.with_scale("50m"))
        ax.add_feature(cfeature.OCEAN.with_scale("50m"))
        ax.add_feature(cfeature.COASTLINE)
        ax.add_feature(cfeature.BORDERS)
        

    else:
        fig = None

    # extend
    if map_extent is not None:
        ax.set_extent(map_extent)
    # plot geopandas data frame
    if crs != "PlateCarree":
        gpd_df = gpd_df.to_crs(proj.get(crs)[0])

    if kdp:
        sns.kdeplot(
                      x=gpd_df['geometry'].x,
                      y=gpd_df['geometry'].y,  # y-axis
                      cmap="viridis",
                      shade=True,
                      thresh=0.05,
                      bw_method=bw,
                      # transform = proj.get(crs)[1],
                      ax = ax,
                  )
    else:
        gpd_df.plot(ax=ax, marker='o', color=color,
             markersize=markersize, alpha=alpha)
        if label is not None:
            ax.scatter([],[],marker='o', color=color,
                s=50, label = label)
    # add gridlines
    ax.gridlines()

    if title is not None:
        ax.set_title(title, size=16)
    # fig.tight_layout()
    return fig, ax

def minmax_scaler(series, lower_bound, upper_bound):
    s_min = series.min()
    s_max = series.max()

    return lower_bound + (series - s_min) * (upper_bound - lower_bound) / (s_max - s_min)