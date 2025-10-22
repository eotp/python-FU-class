df_unstack = pd.read_csv('../data/data_unstack.csv')

print(df_unstack)

df_unstack = df_unstack.groupby(['Year', 'Names'])['Money'].sum()

print(df_unstack)

df_unstack2 = df_unstack.unstack()

df_unstack2