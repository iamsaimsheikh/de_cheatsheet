import pandas as pd

'''
Other formats
- read_parquet
- read_xlsx
'''

df = pd.read_csv('./data/coffee.csv')

# can also ready through urls
coffee = pd.read_csv("https://raw.githubusercontent.com/KeithGalli/complete-pandas-tutorial/refs/heads/master/warmup-data/coffee.csv")

# loc - accessing data | df.loc[#rows, #columns]
loc_df = coffee.loc[coffee['Units Sold'] > 0, ['Day','Coffee Type','Units Sold']] # works with column names
iloc_df = coffee.iloc[:,0:3] # works with indexes

# coffee.MultiIndex = coffee['Day']
# print(loc_df.groupby('Day').sum()) # simple groupby
# print(loc_df.groupby(level=0).sum()) # MultiIndex

coffee.rename(columns={
    'Day':'day',
    'Coffee Type': 'coffee_type',
    'Units Sold': 'units_sold'
}, inplace= True)

coffee['units_sold'] = coffee['units_sold'].apply(lambda x: x * 2)

# Sorting
coffee = coffee.sort_values(['units_sold','coffee_type'], ascending= False)

# Simple Iterrows looping
for index, row in coffee.iterrows():
    # print(row)
    None
    
    

