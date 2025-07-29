import pandas as pd

bios = pd.read_csv('./data/bios.csv')
bios.info()

# Filter using columns
print(bios.loc[bios['height_cm'] > 220])

# A shorthand syntax
print(bios[bios['height_cm'] > 215][['name','height_cm']])

# Multiple conditions
print(bios[(bios['height_cm'] > 220) & (bios['weight_kg'] > 115)])

# For Strings | can use regex r'
print(bios[bios['name'].str.contains("Keith|patrick", case= False)])

# isin()
print(bios[bios['born_country'].isin(["USA", "FRA"])])

# using query
print(bios.query('born_country == "USA" and born_city == "Seattle"'))