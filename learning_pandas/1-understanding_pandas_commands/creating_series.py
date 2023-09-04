# importing pandas framework
import pandas as pd

# Creating a Series using a list
a = [1, 7, 2]
myver = pd.Series(a)
print(myver)
print(type(myver))

# printing my serie from index
print(myver[0])

# Creating a Series and telling what the indexes are
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)
print(type(myvar))

# printing my serie using the index that i defined before
print(myvar["z"])

# Creating a Series with a dict
calories = {"day1": 450, "day2": 250, "day3": 800}
myseries_calories = pd.Series(calories)
print(myseries_calories)
print(type(myseries_calories))

# you can specify only the datas you wanto to use in your serie
my_specific_calories = pd.Series(calories, index=["day2", "day3"])
print(my_specific_calories.to_string())
print(type(my_specific_calories))



