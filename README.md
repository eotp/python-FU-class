# Main repository for the Python class at FU Berlin, summer semester  2023

Dates, location and outline of the class are presented [here](https://www.fu-berlin.de/vv/de/lv/799751).
Starts at 13:15 and ends at 16:30 CET

## Content

- 01 - 2023/04/28

  - Introduction into computational thinking
  - Programming languages and IDEs
  - Why Python?

- 02 - 2023/05/05

  - Python 101

- 03 - 2023/05/12

  - Python 101 continued
  - Plotting with Python

- 04 - 2023/05/19 

  - Introduction to `pandas`
  - Simple data analysis using `pandas`

- 05 - 2023/05/26

  - Pandas recap
  - Simple data analysis using `pandas`
  - Reporting using `jupyterbook`

- 06 - 2023/06/02

  - Exploratory data analysis (EDA)
  - Study project - Powerplants

- 07 - 2023/06/09

  - Study project - Powerplants (Group Session)

- 08 - 2023/06/16 
  - Object Oriented Programming (OOP)
  - (**Submission deadline: 2023/03/19**)
  
- 09 - 2023/06/23 
  - Presentations study projects 

- 10 - 2023/06/30
  
  - Interpolation and curve fitting
  - Inferential statistics
  - Population vs. sample statistics
  - Central Limit Theorem
  - Point and interval estimates (confidence intervals)
  - Hypothesis testing
  - Bootstrapping
  - Introduction to Machine Learning
  - Skipped:
    - Regression analysis
    - Logisitic regression
    - Hyperparamter tuning
    - Polynomial Regression

* 11 - 2023/07/07

  - `Spyder IDE`
  - Dashboarding with `streamlit`
  - Creating dynamic Maps with `folium` 

* 12 - 2023/07/14
  
  - Web scraping
  - Wordclouds

* 13 - 2023/07/21 [opt]

  - Feedback round
  - APIs (FastAPI)
  
---

In order to re-run the class materials I encourage you to use the [conda](https://conda.io/docs/) package manager. Once installed, create an environment and install all required dependencies on your machine by typing

`conda env create -f environment.yml`

into your console (_Windows users: please use the Anaconda Powershell Prompt_). You activate your new environment by typing

`conda activate fupy`

Then you are ready to go (if you are stuck check out the [conda documentation site](https://conda.io/docs/user-guide/tasks/manage-environments.html#)). Alternatively, you may launch [binder](https://mybinder.org/) to get a reproducible executable environment immediately in your browser. Simply click the _launch binder_ icon below.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/eotp/python-FU-class/master?urlpath=lab) (*Note that this link  points to the master branch*)

---

> We should mention that the conda environments created during this course will take up a lot of space!
> Feel free to run `conda env list` to display all created environments and delete them if you choose using `conda env remove -n env_name`.
> Remember that you can always recreate any of the environments using `conda env create -f environment.yml` in any given sub- or the root-directory of this repo. 
