# Mit loc durchlaufen
for i in range(len(df_data)):
    name = df_data.loc[i, 'Name']
    alter = df_data.loc[i, 'Alter']
    geschlecht = df_data.loc[i, 'Geschlecht']
    print(f"{name} ist {alter} Jahre alt und {geschlecht}.")
    
print('----'*30)
    
# Mit iloc durchlaufen
for i in range(len(df)):
    name = df_data.iloc[i, 0]
    alter = df_data.iloc[i, 1]
    geschlecht = df_data.iloc[i, 2]
    print(f"{name} ist {alter} Jahre alt und {geschlecht}.")