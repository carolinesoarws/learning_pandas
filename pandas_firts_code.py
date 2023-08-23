import pandas as pd

# My first pandas code
mydataset = {
    "colors": ["Branco", "Roxo", "Amarelo"],
    "passing": [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print(myvar)
print(type(myvar))
