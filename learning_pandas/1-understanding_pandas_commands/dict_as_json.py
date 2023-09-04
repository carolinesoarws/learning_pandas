# importing panda framework
import pandas as pd

# simples json
data = {
  "Duration": {
    "0": 60,
    "1": 60,
    "2": 60,
    "3": 45,
    "4": 45,
    "5": 60
  },
  "Pulse": {
    "0": 110,
    "1": 117,
    "2": 103,
    "3": 109,
    "4": 117,
    "5": 102
  },
  "Maxpulse": {
    "0": 130,
    "1": 145,
    "2": 135,
    "3": 175,
    "4": 148,
    "5": 127
  },
  "Calories": {
    "0": 409,
    "1": 479,
    "2": 340,
    "3": 282,
    "4": 406,
    "5": 300
  }
}
# Creating the dataframe
df_dict = pd.DataFrame(data)

# printing my dataframe
print(df_dict)
print(df_dict.to_string())
print(type(df_dict))

# you can also use the function json_normalize to create a DataFrame from a json
df_dict_from_json = pd.json_normalize(data)
print(df_dict_from_json)
print(df_dict_from_json.to_string())



