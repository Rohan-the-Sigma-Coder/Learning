import pandas as pd

df = pd.read_csv('data.csv')

x = df.corr()

print(x)