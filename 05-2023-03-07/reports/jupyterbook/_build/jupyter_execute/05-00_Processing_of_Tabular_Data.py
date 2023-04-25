#!/usr/bin/env python
# coding: utf-8

# # Challenge: Processing of Tabular Data 

# __Import Statements__

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt


# ## Read the data

# > ### Challenge: Read the `IHME_GBD_2016_POPULATION_ESTIMATES_1990_2016_Y2017M09D14.CSV` file stored in the `../data/` folder and store it to a variable namend `pop`. _Hint: Use the_ `pd.read_csv` _function._ 

# In[2]:


## your code here
pop = pd.read_csv("../data/IHME_GBD_2016_POPULATION_ESTIMATES_1990_2016_Y2017M09D14.CSV")
pop


# In[3]:


# %load ../src/_solutions/tab_data01.py


# ## Inspect the data

# > ### Challenge: Inspect the data by 
# * printing the column names
# * counting the number of unique entries in the `location_name` column
# * printing some location names
# * figuring out the unique categories for the `sex_name` and `age_group` columns
# 

# 
# ### Exploratory Data Analysis

# * printing the column names

# In[4]:


## your code here
pop.columns


# * counting the number of unique entries in the `location_name` column

# In[5]:


## your code here
pop["location_name"].nunique()


# * printing some location names

# In[6]:


## your code here
pop["location_name"].sample(10)


# * figuring out the unique categories for the `sex_name` and `age_group` columns

# In[7]:


## your code here
pop["sex_name"].unique()


# In[8]:


## your code here
pop["age_group_name"].unique()


# In[9]:


# %load ../src/_solutions/tab_data02.py


# ## Analyzing a subset of the dataset

# > ### Challenge: Subset the data set based on age groups, location and sex as given below and save the resulting  data frame to a variable called `pop_subset`. 

# __Subsetting__

# In[10]:


ages = ['5-14 years', '15-49 years', '50-69 years','70+ years']
location = ["Germany", "France", "Italy"]
sex = ['Male', 'Female']


# In[11]:


## your code here
cond = (
    pop["age_group_name"].isin(ages) & 
    pop["location_name"].isin(location) & 
    pop["sex_name"].isin(sex)
)

pop_subset = pop.loc[cond,:]
print(pop_subset.shape)
pop_subset.sample(5)


# In[12]:


# %load ../src/_solutions/tab_data03.py


# ### Split-Apply-Combine

# ![](_img/split-apply-combine.svg)
# Image source: [Jake VanderPlas 2016, Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)

# > ### Challenge: Compute the population of Germany, Italy and France for the years 1990 to 2016. _Hint: Use the_ `groupby` _function._
# 

# In[13]:


## your code here
gb = pop_subset.groupby(["year_id", "location_name"])["pop"].sum()
gb


# In[14]:


# %load ../src/_solutions/tab_data04.py


# ## Plotting

# > ### Challenge:    
# Plot how the the population of Germany, Italy and France changed over the years 1990 to 2016. 

# In[15]:


## your code here
gb.unstack().plot(figsize=(14,4))
plt.grid()


# In[16]:


# %load ../src/_solutions/tab_data05.py


# > ### Challenge: Redo the analysis from above but now include Spain in addition to Germany, Italy and France into the analysis.

# ## Solution:
# - Append `'Spain'` into the location list and rerun the code above

# In[17]:


location


# In[18]:


location.append('Spain')
location


# In[19]:


## your code here
cond = (
    pop["age_group_name"].isin(ages) & 
    pop["location_name"].isin(location) & 
    pop["sex_name"].isin(sex)
)

pop_subset = pop.loc[cond,:]
print(pop_subset.shape)
pop_subset.sample(5)


# In[20]:


## your code here
gb = pop_subset.groupby(["year_id", "location_name"])["pop"].sum()
gb


# In[21]:


## your code here
gb.unstack().plot(figsize=(14,4))
plt.grid()


# ***
