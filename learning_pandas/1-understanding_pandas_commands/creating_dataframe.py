# importing pandas framework
import pandas as pd


# Creating a dataframe with 2 series
data = {
    "calories": [430, 500, 780],
    "Duration": [50, 40, 45]
}

myver = pd.DataFrame(data)
print(myver)
print(type(myver))

# To return a specific row using dataframe we must use loc command
print(myver.loc[0])
print(myver.loc[1])


# Return row 0 to 1
print(myver.loc[[0, 1]])

# Return row 1 to 2
print(myver.loc[[1, 2]])


# Giving name to our indexes with a dict
data = {
    "Colors": ["Branco", 'Roxo', "Azul"],
    "Fruta": ["Pitaia", "Acai", "blueberry"]
}

my_df = pd.DataFrame(data, index=["Compra1", "Compra2", "Compra3"])
print(my_df)
print(type(my_df))

# Accesing the indexes of Dataframe by name
print(my_df.loc["Compra1"])
print(my_df.loc[["Compra2", "Compra3"]])

# how to return a DataFrame
print(my_df.to_string())

# Reading a csv
df = pd.read_csv("injury-statistics.csv")
print(df)

# Reading a json file
df = pd.read_json("injury-statistics.json")
print(df)

# how to return the first 10 data of the dataframe
print(df.head(10))
print(df.head())

# Returning the tail of the datadrame
print(df.tail(10))
print(df.tail())

