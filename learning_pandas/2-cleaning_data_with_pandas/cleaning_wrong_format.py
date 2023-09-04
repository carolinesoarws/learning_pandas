# import pandas framework
import pandas as pd

# reading a csv file and creating a DataFrame
my_df = pd.read_csv("data_new.csv")
print(my_df["Date"][22])
print(my_df["Date"][26])
print(my_df.to_string())

"""
# Converting the values to date
# see that in this code we are going to run is not totally functional because we are ruiing in all of the data
df_to_datetime = pd.read_csv("data_new.csv")
df_to_datetime["Date"] = pd.to_datetime(df_to_datetime["Date"])
print(df_to_datetime.to_string())

# if you run the code above you are going to get a error because there is a value in the table is NaN
# To fix that we need  to remove this wrong value first
"""

# 1 - Removing the null value from the data frame

print(my_df)
df = pd.read_csv('data.csv')
df.dropna(inplace=True)
print(df)
df['Date'] = pd.to_datetime(df['Date'], format='mixed')

print(df.to_string())