# Main repository for the Python class at FU Berlin, winter semester 2024-2025 (winter break)
 
Dates, location and outline of the class are presented [here](https://www.fu-berlin.de/vv/de/lv/927201).
Starts at 14:00 and ends at 18:00 CET

## Content

- 01 - 2025/02/19

  - Introduction into computational thinking
  - Programming languages and IDEs
  - Why Python?

- 02 - 2025/02/20

  - Python 101

- 03 - 2025/02/26

  - Python 101 continued
  - Plotting with Python

- 04 - 2025/02/27

  - Introduction to `pandas`
  - Simple data analysis using `pandas`

- 05 - 2025/03/05

  - Pandas recap
  - Reporting using `jupyterbook`

- 06 - 2025/03/06

  - Exploratory data analysis (EDA)
  - Study project - Powerplants

- 07 - 2025/03/12

  - Study project - Powerplants (Group Session)

- 08 - 2025/03/13 
  - Object Oriented Programming (OOP)
  
- 09 - 2025/03/19 
  - Presentations study projects 

- 10 - 2025/03/20
  
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
    - Logistic regression
    - Hyperparameter tuning
    - Polynomial Regression

* 11 - 2025/03/26

  - `Spyder IDE`
  - Dashboarding with `streamlit`
  - Creating dynamic Maps with `folium` 

* 12 - 2025/03/27
  
  - Web scraping
  - Wordclouds


* _skipped_ 13 - 2025/xx/xx 

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
