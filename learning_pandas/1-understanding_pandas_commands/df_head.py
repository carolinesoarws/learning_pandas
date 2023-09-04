# Importing the pandas framework
import pandas as pd

# creating a DataFrame from a csv
df_new = pd.read_csv("../2-cleaning_data_with_pandas/data.csv")

# printing the firsts 10 lines of the dataframe
print(df_new.head(10))
# printing the last 10 lines of the dataframe
print(df_new.tail(10))

# creating a DataFrame from a csv
df_new = pd.read_csv("../2-cleaning_data_with_pandas/data.csv")
# from default the head() function returns the firsts 5 lines from the DataFrame
print(df_new.head())
# from default the tail() function returns the last 5 lines from the DataFrame
print(df_new.tail())

# using the functions info to see information about the data
df_info_csv = pd.read_csv("../2-cleaning_data_with_pandas/data.csv")
print(df_info_csv.info())

