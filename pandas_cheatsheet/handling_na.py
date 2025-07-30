import pandas as pd
import numpy as np

coffee = pd.read_csv('./data/coffee.csv')
coffee.loc[0:2, 'Units Sold'] = np.nan
coffee['Units Sold'] = coffee['Units Sold'].bfill()
coffee.loc[0:2, 'Units Sold'] = np.nan
coffee['Units Sold'].fillna(coffee['Units Sold'].mean().round(2), inplace=True)
