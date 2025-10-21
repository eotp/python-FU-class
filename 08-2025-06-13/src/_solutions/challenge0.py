location.append('Spain')
print(location)

cond = (
    pop["age_group_name"].isin(ages) & 
    pop["location_name"].isin(location) & 
    pop["sex_name"].isin(sex)
)

pop_subset = pop.loc[cond,:]
print(pop_subset.shape)
print(pop_subset.sample(5))

gb = pop_subset.groupby(["year_id", "location_name"])["pop"].sum()
print(gb)

gb.unstack().plot(figsize=(14,4))
plt.grid()