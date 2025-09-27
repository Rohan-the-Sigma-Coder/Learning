import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import random

data = {
    "Name": ["Tom", None, "Jerry", "Spike", "Tyke"],
    "Score": [95, 85, None, 70, 90],
    "Age": [20, 21, 22, None, 20]
}
df = pd.DataFrame(data)

print(df.isnull().sum())

df['Name'].dropna(inplace = True)

print(df)

data = {
    'names': ['Sachin', 'Monika', 'Rohan', 'Eshan'],
    'age': [43, 42, 14, 13],
}
data2 = ['Sachin', 'Monika', 'Rohan', 'Eshan']
data3 = {'Sachin': 43, 'Monika': 42, 'Rohan': 14, 'Eshan': 13}

dataframe = pd.DataFrame(data)

series = pd.Series(data3, index = ['Sachin', 'Rohan'])

df = pd.read_csv('data.csv')
counter = 0

average_pulse = round(df['Pulse'].mean(), 2)

average_max_pulse = round(df['Maxpulse'].mean(), 2)

for x in df.index:
    if df.loc[x, 'Duration'] > 50:
        counter += 1

print(counter)
print(average_pulse, average_max_pulse)
print(df['Duration'].head(10), df['Calories'].head(10))
df.fillna({'Calories': df['Calories'].mean()}, inplace=True)

for i in df.index:
    if df.loc[x, 'Maxpulse'] > 170:
        df.drop(x, inplace=True)

print(df.to_string())

for a in df.index:
    if 40 <= df.loc[a, 'Duration'] <= 60 and df.loc[a, 'Calories'] > 400:
        print(df.loc[a])

for b in df.index:
    if df.loc[b, 'Pulse'] > 120 and df.loc[b, 'Maxpulse'] < 150:
        print(df.loc[b])


df.fillna({'Calories': 0}, inplace = True)
print(df.sort_values(by='Calories').tail(5).to_string())
print(df.sort_values(by='Calories', ascending=False).to_string())
print(df.groupby('Duration')['Calories'].mean())
print(df.groupby('Duration')['Maxpulse'].max())
df['Calories_per_minute'] = df['Calories'] / df['Duration']
print(df.to_string())
print(df.corr())



