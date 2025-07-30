import pandas as pd

coffee = pd.read_csv("./data/coffee.csv")

# shift

coffee["Price"] = coffee["Coffee Type"].map({"Espresso": 3.5, "Latte": 4.5})
coffee["Revenue"] = coffee["Price"] * coffee["Units Sold"]
latte = coffee[coffee['Coffee Type'] == 'Latte']
latte['Previous Day Revenue'] = latte['Revenue'].shift(1)
latte['Delta Revenue'] = latte['Previous Day Revenue'] - latte['Revenue']

# rank
latte['Revenue Rank'] = latte['Revenue'].rank()

# rolling

latte['3day'] = latte['Units Sold'].rolling(3).sum()
print(latte)
