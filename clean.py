import pandas as pd
import csv

df = pd.read_csv("final.csv")
print(df.shape)

del(df["Star_name"])
del(df["Distance"])
del(df["Mass"])
del(df["Radius"])

print(list(df.shape))

df.to_csv('main.csv')
