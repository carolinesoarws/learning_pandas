import pandas as pd


df = pd.read_csv("data.csv")
print(df.to_string())

# Return max of rows

print(pd.options.display.max_rows)

#you can chagded the value of the max rows that can br shown

pd.options.display.max_rows = 500
df_data = pd.read_csv("data.csv")
print(df_data.to_string())
