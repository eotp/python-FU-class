gb = pop_subset.groupby(["year_id", "location_name"])["pop"].sum()
gb = gb.unstack()
gb