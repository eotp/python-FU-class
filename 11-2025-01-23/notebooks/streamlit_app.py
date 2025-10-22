{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3b656bf6-64c8-437e-a829-86764f16277a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import geopandas as gpd\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Load data\n",
    "world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))\n",
    "\n",
    "# Create plot\n",
    "fig, ax = plt.subplots(figsize=(10, 6))\n",
    "world.plot(ax=ax, color='lightgray', edgecolor='black')\n",
    "ax.set_title('World Map')\n",
    "\n",
    "# Display plot in Streamlit\n",
    "st.pyplot(fig)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
