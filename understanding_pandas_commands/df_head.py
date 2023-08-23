import pandas as pd

df_new = pd.read_csv("data.csv")
print(df_new.head(10))
print(df_new.tail(10))

df_new = pd.read_csv("data.csv")
print(df_new.head())
print(df_new.tail())

# using the functions info to see information about the data

df_info_csv = pd.read_csv("data.csv")
print(df_info_csv.info())

