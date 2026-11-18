# Assignment 3 - Question 3
# DataFrame Slicing using Pandas

import pandas as pd

data = {
    "Tid": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Refund": ["Yes", "No", "No", "Yes", "No",
               "No", "Yes", "No", "No", "No"],
    "Marital Status": ["Single", "Married", "Single", "Married",
                       "Divorced", "Married", "Divorced", "Single",
                       "Married", "Single"],
    "Taxable Income": ["125K", "100K", "70K", "120K", "95K",
                       "60K", "220K", "85K", "75K", "90K"],
    "Cheat": ["No", "No", "No", "No", "Yes",
              "No", "No", "Yes", "No", "Yes"]
}

df = pd.DataFrame(data)

# (i) Select rows from index 3 to 7
print("Q3(i): Rows from index 3 to 7")
print(df.iloc[3:8])

# (ii) Select rows 4 to 8 and columns 2 to 4
print("\nQ3(ii): Rows 4 to 8 and Columns 2 to 4")
print(df.iloc[4:9, 2:5])

# (iii) Select all rows and columns 1 to 3
print("\nQ3(iii): All Rows and Columns 1 to 3")
print(df.iloc[:, 1:4])