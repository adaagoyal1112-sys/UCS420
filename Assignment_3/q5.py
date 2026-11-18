# Assignment 3 - Question 5
# Delete row 4 and column 3 from Iris dataset

import pandas as pd

# Read CSV file
df = pd.read_csv("Assignment_3/Iris.csv")

print("Original DataFrame:")
print(df)

# Delete row at index 4
df = df.drop(index=4)

# Delete column at index 3 (PetalLengthCm)
df = df.drop(columns=df.columns[3])

print("\nQ5: DataFrame After Deleting Row 4 and Column 3")
print(df)