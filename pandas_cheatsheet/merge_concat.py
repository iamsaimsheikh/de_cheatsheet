import pandas as pd

bios = pd.read_csv("./data/bios.csv")
noc = pd.read_csv("./data/noc_regions.csv")

# merging - horizontal on a column 
bios = pd.merge(bios,noc, left_on='born_country', right_on='NOC', how='left')
bios.rename(columns={"region":"born_country_full"})

# concat - append rows
usa_df = bios[bios['born_country'] == 'USA'].copy()
gbr_df = bios[bios['born_country'] == 'GBR'].copy()

bios = pd.concat([usa_df,gbr_df])
print(bios.head())