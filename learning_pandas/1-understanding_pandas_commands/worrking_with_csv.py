# importing pandas framework
import pandas as pd

# reading a csv e already transforming into a DataFrame
df = pd.read_csv("../2-cleaning_data_with_pandas/data.csv")
print(df.to_string())

# Return max of rows
print(pd.options.display.max_rows)

# you can chagded the value of the max rows that can br shown

pd.options.display.max_rows = 500
df_data = pd.read_csv("../2-cleaning_data_with_pandas/data.csv")
print(df_data.to_string())
