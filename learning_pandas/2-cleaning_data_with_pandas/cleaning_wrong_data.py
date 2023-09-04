# importing pandas framework
import pandas as pd

# One way is replacing the value with the index
# reading from a csv and already transforming into a Dataframe
df = pd.read_csv("data.csv")
print(df.to_string())
# changing the value of a fild in the datafrmae
df.loc[7, 'Duration'] = 45
print(df.to_string())

# you can make something more\
# Validating if the dataframe has a value in the durating column higher then 120
# then changing the value to 120
df = pd.read_csv("data.csv")
print(df.to_string())
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120
print(df.to_string())

# doing the same as the code above then updating the value of the Dataframe
# with the command inplace
print(df.to_string())
for x in df.index:
    if df.loc[x, "Duration"] >= 120:
        df.drop(x, inplace=True)
print(df.to_string())
