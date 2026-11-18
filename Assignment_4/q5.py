# Assignment 4 - Question 5
# Roll Number: 1024170122

import pandas as pd

# Read the FAQ dataset saved in Q4
df = pd.read_csv("Assignment_4/1024170122_faq_data.csv")

print("Q5: FAQ Count Per Category")

# Group FAQs by category and count entries
category_counts = df.groupby("category").size()

print(category_counts)