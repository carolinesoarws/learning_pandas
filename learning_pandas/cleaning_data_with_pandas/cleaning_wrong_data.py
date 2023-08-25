import pandas as pd

# One way is replacing the value with the index

df = pd.read_csv("data.csv")
print(df.to_string())
df.loc[7, 'Duration'] = 45
print(df.to_string())

df = pd.read_csv("data.csv")
print(df.to_string())
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120
print(df.to_string())


print(df.to_string())
for x in df.index:
    if df.loc[x, "Duration"] >= 120:
        df.drop(x, inplace=True)
print(df.to_string())
