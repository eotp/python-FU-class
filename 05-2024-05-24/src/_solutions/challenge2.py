ages = ['5-14 years','70+ years']
location  = ['Germany']
sex = ['Male', 'Female']

cond = (
    pop["age_group_name"].isin(ages) & 
    pop["location_name"].isin(location) & 
    pop["sex_name"].isin(sex)
)

pop_subset2 = pop.loc[cond,:]
print(pop_subset2.shape)
print(pop_subset2.sample(5))

gb2 = pop_subset2.groupby(["year_id", "age_group_name"])["pop"].sum()
print(gb2)

gb2.unstack().plot()