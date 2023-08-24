import pandas as pd

# Returning a new data frame with no empty cells
df = pd.read_csv("data.csv")
new_df = df.dropna()
print(new_df)
print(new_df.info())



# by default the dropna returns a new data frame, we can changed it

df_new = pd.read_csv("data.csv")
df.dropna(inplace=True)
print(df.to_string())


#Replacing the null  to another value
df_replacing = pd.read_csv('data.csv')
df_replacing.fillna(130, inplace=True)
print(df_replacing)


#   Replacing from a specific column
df_calories = pd.read_csv("data.csv")
df_calories["Calories"].fillna(130, inplace=True)
print(df_calories.to_string())


# calculating the average value (media) of a column
# and replacing a null value with it
df_mean = pd.read_csv("data.csv")
new_df_mean = df["Calories"].mean()
print(df["Calories"].mean())
df_mean["Calories"].fillna(new_df_mean, inplace=True)


# Calculate de MEDIAN and replace any empty value with it
# Median - the value in the middle
df_median = pd.read_csv("data.csv")
x = df["Calories"].median()
print(x)
df["Calories"].fillna(x, inplace=True)
print(df["Calories"].to_string())


# Calculating the mode
# Mode - the value that appears most frequenttly
df_mode = pd.read_csv("data.csv")
x = df["Calories"].mode()[0]
print(x)
df["Calories"].fillna(x, inplace = True)
print(df["Calories"].to_string)
