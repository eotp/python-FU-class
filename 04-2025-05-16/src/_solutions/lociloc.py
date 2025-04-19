# Filtern mit loc
weibliche_personen = df_data.loc[df_data['Geschlecht'] == 'weiblich']
alte_personen = df_data.loc[df_data['Alter'] > 30]

# Filtern mit iloc
weibliche_personen = df_data.iloc[(df_data['Geschlecht'] == 'weiblich').values, :]
alte_personen = df_data.iloc[(df_data['Alter'] > 30).values, :]

print(weibliche_personen)
print(alte_personen)