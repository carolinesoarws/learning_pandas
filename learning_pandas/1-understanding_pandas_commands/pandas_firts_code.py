# Importing pandas module
import pandas as pd

# My first pandas code
# Creating a dataset to create a data frame
mydataset = {
    "colors": ["Branco", "Roxo", "Amarelo"],
    "passing": [3, 7, 2]
}

# Creating a DataFrame
myvar = pd.DataFrame(mydataset)
print(myvar)
print(type(myvar))
