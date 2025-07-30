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



