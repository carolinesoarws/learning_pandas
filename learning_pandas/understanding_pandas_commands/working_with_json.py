import pandas as pd

df_json = pd.read_json("data.json")
print(df_json.to_string())
