# importing pandas framework
import pandas as pd

# reading a Json and already transforming into a dataframe
df_json = pd.read_json("data.json")
print(df_json.to_string())
print(type(df_json))
