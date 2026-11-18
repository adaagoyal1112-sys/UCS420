# Assignment 3 - Question 6
# Employee Dataset Using Pandas

import pandas as pd

# Create employee dataset
data = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department": ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age": [29, 34, 41, 28, 38],
    "Salary": [50000, 70000, 65000, 55000, 60000],
    "Years_of_Experience": [4, 8, 10, 3, 12],
    "Joining_Date": [
        "2020-03-15", "2017-07-19", "2013-06-01",
        "2021-02-10", "2010-11-25"
    ],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Bonus": [5000, 7000, 6000, 4500, 5000],
    "Rating": [4.5, 4.0, 3.8, 4.7, 3.5]
}

df = pd.DataFrame(data)

# Save original dataset
df.to_csv("Assignment_3/employees.csv", index=False)

print("Original Employee Dataset:")
print(df)

# (a) Shape of DataFrame
print("\nQ6(a): Shape of DataFrame")
print(df.shape)

# (b) Summary of DataFrame
print("\nQ6(b): DataFrame Information")
df.info()

# (c) Descriptive Statistics
print("\nQ6(c): Descriptive Statistics")
print(df.describe())

# (d) First 5 and Last 3 Rows
print("\nQ6(d): First 5 Rows")
print(df.head())

print("\nLast 3 Rows")
print(df.tail(3))

# (e) Statistical Calculations
print("\nQ6(e): Statistical Calculations")

print("Average Salary:", df["Salary"].mean())
print("Total Bonus:", df["Bonus"].sum())
print("Youngest Employee Age:", df["Age"].min())
print("Highest Performance Rating:", df["Rating"].max())

# (f) Sort by Salary in Descending Order
print("\nQ6(f): Salary in Descending Order")
print(df.sort_values(by="Salary", ascending=False))

# (g) Add Performance Category
print("\nQ6(g): Performance Category")

def performance_category(rating):
    if rating >= 4.5:
        return "Excellent"
    elif rating >= 4.0:
        return "Good"
    else:
        return "Average"

df["Performance"] = df["Rating"].apply(performance_category)

print(df[["Name", "Rating", "Performance"]])

# (h) Identify Missing Values
print("\nQ6(h): Missing Values")
print(df.isnull().sum())

# (i) Rename Employee_ID to ID
print("\nQ6(i): Rename Column")

df.rename(columns={"Employee_ID": "ID"}, inplace=True)

print(df.columns)

# (j) Filter Employees
print("\nQ6(j): Employees with More Than 5 Years Experience")
print(df[df["Years_of_Experience"] > 5])

print("\nEmployees in IT Department")
print(df[df["Department"] == "IT"])

# (k) Add Tax Column
print("\nQ6(k): Add Tax Column")

df["Tax"] = df["Salary"] * 0.10

print(df[["Name", "Salary", "Tax"]])

# (l) Save Modified DataFrame
print("\nQ6(l): Save Modified Dataset")

df.to_csv("Assignment_3/employees_modified.csv", index=False)

print("Modified dataset saved successfully!")
