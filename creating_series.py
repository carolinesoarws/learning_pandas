import pandas as pd

a = [1, 7, 2]
myver = pd.Series(a)
print(myver)
print(type(myver))

# printing my serie from index
print(myver[0])

myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)
print(type(myvar))

#printing my serie using the label
print(myvar["z"])

# Creating a Dictionary as a Serie
calories = {"day1": 450, "day2": 250, "day3": 800}

myseries_calories = pd.Series(calories)
print(myseries_calories)
print(type(myseries_calories))


#you can specify only the datas you wanto to use in your serie
my_specific_calories = pd.Series(calories, index=["day2", "day3"])




