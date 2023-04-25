#!/usr/bin/env python
# coding: utf-8

# # Temperature anomalies - A prelimnary analysis

# ## Introduction
# 
# In this section we explore a real world data set. We consider land-surface temperature anomalies provided by [__Berkeley Earth__](http://berkeleyearth.org/), an independent non-profit entity, which established an [open database](http://berkeleyearth.org/data/) with air temperature data of different spatial and temporal scales. 
# 
# ### Objectives
# 
# #### 1. We explore the global temperature anomaly from 1750 to present.
# #### 2. We construct an informative time series plot for the global temperature anomaly.   
# #### 3. We write a function to plot temperature anomalies for any given country/region of the database.
# #### 4. Save a nice locking time series plot to disk.
# 

# ***
# ## Getting started
# 
# We start by importing the packages/libraries that we will need for these tasks.

# In[ ]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

# this call causes the figures to be plotted below the code cells
get_ipython().run_line_magic('matplotlib', 'inline')


# ***
# ## Objective 1 - Explore the global temperature anomaly from 1750 to present
# ### Objective 1.0 - Take a first look at the data 

# The land-surface average temperature data set produced by the Berkeley Averaging method is found online:
# 
# http://berkeleyearth.lbl.gov/auto/Global/Complete_TAVG_complete.txt
# 
# We already downloaded the data set for you. It is stored in the `../data` folder under the filename `Complete_TAVG_complete.txt`.
# 
# 
# 
# #### **Challenge 1: Inspect the first 50 lines of the raw text file and read the metadata to get familiar with the nature of the data set and its generation. (Time: 3 Minutes)**   
# 
# >Hint: To run a shell command from within the `Jupyter Notebook` use the `!` magic.    
# ##### **macOS/Linux**: 
# - In order to look at the first 50 lines of the text file you may use the `bash` command 
# 
# ```bash
# !head -50 PATH_TO_FILE/FILENAME
# ```
# 
# ##### **Windows**: 
# - In order to use the `!` magic with powershell please run 
# ```python
# import os
# os.environ['comspec']='powershell.exe'
# ```
# 
# - In order to look at the first 50 lines of the text file you may use the `powershell` command 
# 
# ```powershell
# !gc PATH_TO_FILE/FILENAME -head 50
# ```
# 

# In[ ]:


## your code here ...


# ##### **macOS/Linux Solution**

# In[ ]:


# %load ../src/_solutions/time_series_analysis_macos_linux


# ##### **Windows Solution**

# In[ ]:


# %load ../src/_solutions/time_series_analysis_windows


# The dataset is a good example of datasets used in science: text format, good documentation, human readable but a bit harder to deal with programmatically (e.g. column names as comments instead of strict CSV).   

# ***
# 
# ### Objective 1.1 - Load the data set with `pandas`
# 
# The `pandas` library offers several data import operations. In this section we use the `pd.read_csv()` function. This function is very powerful and ships with many additional arguments to parse data, given in a variety of forms. 
# 
# The get familiar with the `pd.read_csv()` function, we look up the documentation to gain some intuition. 
# 
# #### **Challenge 2: Type `?pd.read_csv` into the cell below and run the cell.**

# In[ ]:


## your code here ...


# In[ ]:


# %load ../src/_solutions/time_series_analysis_020.py


# Don't be intimidated by the number of available arguments to the function call.    
# Note that most of the arguments come with a pre-defined default value, hence we focus on those few arguments, for which we actually need to provide the input.
# 

# #### **Challenge 3: Load the file `Complete_TAVG_complete.txt` using the `pd.read_csv()` function. Build up the function call sequentially in order to fulfill our particular needs. (Time: 8 Minutes)**
# * Start by providing the path to the file to the `pd.read_csv()` function.
# * Use the `comment` argument, to specify which lines should not be parsed. Note that not defining the `comment` argument will cause an error for this dataset!
# * Set `delim_whitespace=True` to specify that whitespace (e.g. ``' '`` or ``'    '``) will be used as the column separator.
# * Set `header=None` to indicate that the first line is not a header line. 
# * Set the `usecols` argument to pick a subset of the columns.  For the purpose of this tutorial we are only interested in the columns `"year"`, `"month"`, `"anomaly"`, and `"uncertainty"`. *Hint: Our columns of interest are at column indices `0`, `1`, `2`, `3`* 
# * Specify column names by using the `names` argument (`["year", "month", "anomaly", "uncertainty"]`).

# In[ ]:


## your code here ...


# In[ ]:


# %load ../src/_solutions/time_series_analysis_030.py


# * For the sake of reproducibility we refactor our code and write a function called `read_temp_data`, with only one input argument, the `FILEPATH`.  _Note that we have already written the function for you. The code is stored in the folder_ `../src/_solutions/` _with the filename_ `time_series_analysis_f01.py`. We use the magic function `%load` to load the Python file.
# 
#       %load ./src/_solutions/time_series_analysis_f01.py
# 
# _Uncomment the code cell below and execute the code cell once to import the file and once more to actually run the code._ 

# In[ ]:


# %load ../src/_solutions/time_series_analysis_f01.py


# * Apply the `read_temp_data()` function to create a `DataFrame` object containing the global land surface temperature anomaly provided by the open database of Berkeley Earth and store it into a variable called `data_raw`.

# In[ ]:


FILEPATH = '../data/Complete_TAVG_complete.txt'
data_raw = read_temp_data(FILEPATH)
data_raw


# In[ ]:


## use the sample method to look at 10 rows at random
data_raw.sample(10)


# ***
# ### Objective 1.2 - Exploratory data analysis
# 
# In this section we work with time series data; hence, we want to make use of the full functionality for time series analysis provided by the `pandas` library. Consequently, we provide `pandas` an appropriate time-based index.

# In[ ]:


## make a copy of the DataFrame object
data_ts = data_raw.copy()


# In[ ]:


data_ts.head()


# In[ ]:


# index of the DataFrame object
data_ts.index


# In[ ]:


# data types in the DataFrame object
data_ts.dtypes


# #### **Challenge 4: Generate a time based index by combining the columns `year` and `month`. (Time: 5 Minutes)**
# * Apply the `astype()` method on a `pd.Series` object to convert an `int` into a `string`.
# * Concatenate (`+`) the columns `year` and `month` (both being `string` objects) with a `"-"` in between and apply `pd.to_datetime()` to generate a `datetime` object.
#     - _Note: you will need two concatenations: One to concatenate `year` and `"-"` and another to contatenate the result with `month`_
# * Chain the `datetime` attribute and the `to_period('M')` method together and to generate an index (`PeriodIndex`).
# * Assign the `PeriodIndex` back to the `DataFrame` object `data_ts` using `set_index()`.

# In[ ]:


## your code here ...


# In[ ]:


# %load ../src/_solutions/time_series_analysis_040.py


# * For the sake of reproducibility we refactor our code and write a function called `monthly_index`, with only one input argument, a `DataFrame` object. _Note that we have already written the function for you._ 
# 
#       %load ../src/_solutions/time_series_analysis_f02.py
#       
# _Uncomment the code cell below and execute the cell once to import the file and once more to actually run the code._ 
# 

# In[ ]:


# %load ../src/_solutions/time_series_analysis_f02.py


# * Apply the `monthly_index()` function to create a `DataFrame` with a monthly `PeriodIndex` and store it into a variable called `data_monthly`.

# In[ ]:


data_monthly = monthly_index(data_raw)
data_monthly.head()


# #### **Challenge 5: Print the descriptive statistics of the `anomaly` column. (Time: 2 Minutes)**
# * count
# * mean
# * standard deviation
# * min
# * 25, 50, and 75%-quantile
# * max  
# 
# _Hint: Recall the `describe()` method_
# 
# 

# In[ ]:


##  your code here ...


# In[ ]:


# %load ../src/_solutions/time_series_analysis_050.py


# #### **Challenge 6: Plotting of the distribution of the `anomaly` column. (Time: 3 Minutes)**
# * Plot the distribution of `anomaly` using the `plot.hist()` method (Feel free to play around with the `bins` argument).
# * Plot the distribution of `anomaly` for the periods 1850-1900 and 1950-2000 in one plot 
#     - _Hint: Recall the `loc` method_
#     - _Hint: Recall that you can create `fig` and `ax` objects by running `plt.subplots()`_
#     - _Hint: Recall that you can pass an `ax` object to the plotting function: `plot.hist(ax=ax)`_

# In[ ]:


## your code here ...


# In[ ]:


# %load ../src/_solutions/time_series_analysis_060.py


# ***
# ## Objective 2 -  Construct an informative time series plot for the global temperature anomaly

# The `pandas` library makes plotting very easy. Calling the `plot()` method on a `pd.Series` or `pd.DataFrame` object will create a plot. Note that `pandas` relies on the extremely powerful `matplotlib` library. Refer to the `matplotlib` [gallery](https://matplotlib.org/gallery/index.html) of the [online documentation](https://matplotlib.org/) to get an idea what `matplotlib` can do for you.
# 
# 

# ***
# ### Objective 2.1 -  Construct a simple time series plot of the global temperature anomaly

# #### **Challenge 7: Plot a time series plot of the `anomaly` column. (Time: 3 Minutes)**
# 
# _Hint: Use the `plot()` method_

# In[ ]:


## your code here ... 


# In[ ]:


# %load ../src/_solutions/time_series_analysis_070.py


# ***
# ### Objective 2.2 -  Improve the simple time series plot by computing a 10-year running mean for the `anomaly` and the `uncertainty` columns.

# #### **Challenge 8: Compute a 10-year running mean for the `anomaly` and the `uncertainty` columns and plot them.**
# We compute a running mean by combining the `rolling()`  and the `mean()` method.   (Time: 10 minutes)
# * The `rolling()` method takes several arguments. We need to find an appropriate value for the `window` argument. Further we set `center=True`. 
# * Once we have called the `rolling()` method we chain it with the `mean()` method to compute the 10-year running mean. _Hint: Use the `plot()` method to verify the computation._
# * Repeat the procedure for the `anomaly` and the `uncertainty` columns and add the two columns to the dataframe, denoted as `10-year-anomaly` and `10-year-uncertainty`. 
# * Plot the `anomaly`, the `10-year-anomaly` as well as the `"10-year-uncertainty"` within one single plot. _Hint: Note that the `uncertainty` corresponds to the absolute value of deviation. Compute `10-year-anomaly` $+$ `10-year-uncertainty` and `10-year-anomaly` $-$ `10-year-uncertainty` to get the upper and lower bounds of uncertainty._ 

# Rolling mean demo

# In[ ]:


## compute window length 10 years --> 10 * 12 months
w = 12*10

## compute 10-year-running mean for anomaly and plot the result
rolling_mean_anomaly = data_monthly["anomaly"].rolling(window=w, center=True).mean()

display(rolling_mean_anomaly.head(5))

display(rolling_mean_anomaly.sample(5))


# **Note that for the first years we can't calculate a 10 year mean.**

# In[ ]:


## compute window length 10 years --> 10 * 12 months
w = 12*10

## compute 10-year-running mean for anomaly and plot the result
data_monthly["10-year-anomaly"] = data_monthly["anomaly"].rolling(window=w, center=True).mean()


## your code here ...


# In[ ]:


# %load ../src/_solutions/time_series_analysis_080.py


# * For the sake of reproducibility we refactor our code and write a function called `plot_anomalies`, with two input argument, a `DataFrame` object and a `string`, corresponding to the title of the plot.
# 
# Note that we have already written the function for you. Moreover, we added some boilerplate code the control the figure aesthetics such as `color`, `linewidth`, `linestyle`, fillings (`fill_between`) and opacity (`alpha`); further we added a `title` and axis labels. 
# 
# #### **Challenge 9: Read the code line for line and try to figure out what each line of code is doing. (Time: 5 minutes)**
# *The code is stored in the folder `../src/_solutions/` with the filename `time_series_analysis_f03.py`. We use the magic function `%load` to import the Python file.
# 
#     %load ../src/_solutions/time_series_analysis_f03.py
# 
# *Uncomment the code cell below.*

# In[ ]:


# %load ../src/_solutions/time_series_analysis_f03.py


# * Apply the `plot_anomalies()` function to create a figure.

# In[ ]:


plot_anomalies(data_monthly, 
               title="Global temperature anomaly relative to the period 1951-1980");


# ***
# ## Objective 3 - Write a function to plot temperature anomalies for any given country/region of the database

# In the previous sections we sequentially built up code segments that finally produce an informative time series plot. In this section we refactor our code to become even more generic. We write a function that produces such a time series plot for any given region or country name.
# 
# Again we build up our code base sequentially; however this time, we make use of the functions `read_temp_data()`, `monthly_index()` and `plot_anomalies()`. Hence, reducing the lines of code to write and in addition, our code becomes more readable.

# We follow the procedure outlined below
# 1. Locate the data files (find the correct url) of interest in the open database of [Earth Berkeley](http://berkeleyearth.org/).
# * Load temperature data from the internet and preprocess it using our `read_temp_data()` function.
# * Assign a time based index to the data set using our `monthly_index()` function.
# * Plot the data of interest using our `plot_anomalies()` function.

# ***
# ### Objective 3.1 - Locate the data files (find the correct url) of interest in the open database of [Earth Berkeley](http://berkeleyearth.org/)

# Follow the link below and you see that the temperature data set for each particular country/region can be accessed via an unique url:
# 
# http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/
# 
# Note that Jupyter notebooks allow us to embed an `IFrame` into a notebook cell (see below)
# 

# In[ ]:


from IPython.display import IFrame
IFrame("http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/", width="100%", height=400)


# By investigating the structure of the database we realize that each particular data set can be assessed via an unique url, which may be decomposed into three parts:
# 
# Part 1 - the base url: `http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/...`   
# Part 2 -  the country/region name: `...afghanistan...`, `...africa...` or `...angola...`, among others.   
# Part 3 -  the url suffix: `...-TAVG-Trend.txt`   
# 
# For example, the url for the temperature data set of Germany is 
# 
# `BASE_URL` + `COUNTRY` + `SUFFIX` = http://berkeleyearth.lbl.gov/auto/Regional/TAVG/Text/germany-TAVG-Trend.txt

# #### **Challenge 10: Wrap this idea into a python function called `data_url()`, which takes one input argument, the name of the country/region. (Time: 5 minutes)**
# _Hint: Concatenate `string` objects using the `+` sign_

# In[ ]:


## your code here ...
def data_url(name):
    pass
    return


# In[ ]:


# %load ../src/_solutions/time_series_analysis_100.py


# * What is the url for the temperature data set for Germany?    
# Use the function `data_url()` to build the url for accessing temperature data for Germany. 

# In[ ]:


data_url("germany")


# ***
# ### Objective 3.1, 3.2 and 3.3 - Load temperature data, assign a time based index and plot the data of interest

# Owing to the fact that we consequently refactored our code into python functions, these tasks become fairly easy. We just have to call one function after the other.    
# 
# #### **Challenge 11: Apply `data_url()`, followed by `read_temp_data()`, `monthly_index()` and `plot_anomalies()` to plot the temperature anomaly for Germany from 1750 to present. (Time: 4 minutes)**
# 
# *Note that the `pd.read_csv()` function, built into our `read_temp_data()` function, also accepts an url as input argument and that the  `plot_anomalies()` function awaits two arguments, a `DataFrame` object and a `string` object as `title`.*

# In[ ]:


## your code here ...


# In[ ]:


# %load ../src/_solutions/time_series_analysis_110.py


# * Once again, for the sake of reproducibility we refactor our code and write a function called `plot_country_anomalies`, with one input argument, a `string` object referring to a particular country/region of interest. Note that we have already written the function for you (`time_series_analysis_f04.py`). 
# 
#       %load ../src/_solutions/time_series_analysis_f04.py
#     
# _Uncomment the code cell below._

# In[ ]:


# %load ../src/_solutions/time_series_analysis_f04.py


# #### **Challenge 12: Use the function `plot_country_anomalies()` to plot the temperature anomalies for**
# * `germany`
# * `australia` and
# * `china`   
# (Time: 6 Minutes)
# 

# In[ ]:


## your code here ...


# In[ ]:


# %load ../src/_solutions/time_series_analysis_120.py
## Solution Challenge 12
plot_country_anomalies("germany")
plot_country_anomalies("australia")
plot_country_anomalies("china");


# ***
# 
# ## Objective 4 - Save a time series plot to disk

# Finally, we are done and want to save one of our plots to disk. Therefore we call the `plt.savefig()` function.
# 
# #### **Challenge 13: Create a plot of a country of your choice. Use the function `plt.savefig()` to save the plot to disk. Save the plot as a `.png` file with a resolution of 300 dpi in the folder `../figures/`. (Time: 3 Minutes)**
# 
# 

# In[ ]:


# your code here ...


# In[ ]:


# %load ../src/_solutions/time_series_analysis_130.py


# ***
