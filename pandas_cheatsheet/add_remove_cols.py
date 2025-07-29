import pandas as pd

"""
Other formats
- read_parquet
- read_xlsx
"""

coffee = pd.read_csv("./data/coffee.csv")
bios = pd.read_csv("./data/bios.csv")

coffee["Price"] = coffee["Coffee Type"].map({"Espresso": 4.99, "Latte": 3.99})

# Joint aggregation
# print(coffee.groupby(['Coffee Type', 'Day']).apply(lambda g:(g['Units Sold'] * g['Price']).sum()).reset_index(name="Revenue"))

coffee["Revenue"] = coffee["Price"] * coffee["Units Sold"]
coffee["New Price"] = coffee["Price"].apply(lambda x : x + (0.25 * x))
coffee["Revenue"] = coffee["New Price"] * coffee["Units Sold"]
coffee.drop(columns=['Price'])

# print(coffee.query('Revenue >= 200 and Day == "Friday"'))

# Handling Strings
bios['first_name'] = bios["name"].str.split(" ").str[0]

# Handling datetimes
bios['born_date'] = pd.to_datetime(bios['born_date'])
bios['born_year'] = bios['born_date'].dt.year
bios['born_year'] = bios['born_year'].bfill()
bios['born_year'] = bios['born_year'].astype('int')
print(bios.head())
