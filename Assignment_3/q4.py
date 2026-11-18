# Assignment 3 - Question 4
# Read CSV file and display first five rows

import pandas as pd

df = pd.read_csv("Assignment_3/Iris.csv")

print("Q4: First Five Rows of Iris Dataset")
print(df.head())