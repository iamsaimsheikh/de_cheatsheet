import pandas as pd

bios = pd.read_csv('./data/bios.csv')
coffee = pd.read_csv('./data/coffee.csv')

# value_counts()

print(bios.value_counts()) # - simple value_counts()
print(bios['born_city'].value_counts()) # - specific column
print(bios[bios['born_country'] != 'USA']['born_region'].value_counts()) # - with filters

# groupby

print(coffee.groupby('Coffee Type')['Units Sold'].sum())
print(coffee.groupby(['Coffee Type', 'Day']).sum())

# pivot

pivot = coffee.pivot(columns='Coffee Type', index='Day', values='Units Sold')
print(pivot.sum(axis=0))