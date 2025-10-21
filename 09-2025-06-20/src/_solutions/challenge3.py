ages = ['95 plus']
location  = ['Germany']
sex = ['Male', 'Female']

cond = (
    pop["age_group_name"].isin(ages) & 
    pop["location_name"].isin(location) & 
    pop["sex_name"].isin(sex)
)

pop_subset3 = pop.loc[cond,:]
print(pop_subset3.shape)
print(pop_subset3.sample(5))

gb3 = pop_subset3.groupby(["year_id", "sex_name"])["pop"].sum()
print(gb3)

gb3.unstack().plot()