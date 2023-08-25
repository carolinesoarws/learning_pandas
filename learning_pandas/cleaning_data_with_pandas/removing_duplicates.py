import pandas as pd

# how to discover duplicated rows
df = pd.read_csv("data.csv")
print(df.duplicated())
# removing the duplicates
df.drop_duplicates(inplace=True)
print(df.duplicated())
print(df.to_string())
