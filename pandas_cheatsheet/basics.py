import pandas as pd

df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], columns= ["A","B","C"])

# to check columns
print(df.columns)

# access data start and end
df.head()
df.tail()

# get information
df.info()
df.describe()

# get unique
df.nunique()
df['A'].unique()