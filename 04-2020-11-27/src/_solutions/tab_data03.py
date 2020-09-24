cond = (
    pop.age_group_name.isin(ages) & 
    pop.location_name.isin(location) & 
    pop.sex_name.isin(sex)
)

pop_subset = pop.loc[cond,:]
print(pop_subset.shape)
pop_subset.sample(5)
