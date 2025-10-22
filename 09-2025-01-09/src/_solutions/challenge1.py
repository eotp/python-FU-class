gb1 = pop_subset.groupby(["year_id", "location_name",'age_group_name'])["pop"].sum()
print(gb1)

gb1.unstack().unstack().plot(figsize=(14,4))