import pandas as pd
import matplotlib.pyplot as plt

# Reading a csv file then creating a Dataframe
df = pd.read_csv("data.csv")
print(df.corr())

df = pd.read_csv('data.csv')
df.plot()
plt.show()