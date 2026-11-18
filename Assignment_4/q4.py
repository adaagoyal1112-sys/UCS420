# Assignment 4 - Question 4
# Roll Number: 1024170122

import pandas as pd

roll_no = "1024170122"
categories = ["billing", "account", "general"]

fixed_entries = [
    {
        "question": "what is the annual fee",
        "answer": "The annual fee is Rs 500.",
        "keywords": "fee cost price charge",
        "category": "billing"
    },
    {
        "question": "how to reset password",
        "answer": "Go to Settings > Reset Password.",
        "keywords": "password reset login",
        "category": "account"
    },
    {
        "question": "what are your working hours",
        "answer": "We are open 9 AM to 5 PM.",
        "keywords": "hours timing open time",
        "category": "general"
    },
    {
        "question": "how can i pay the fee",
        "answer": "You can pay via UPI, card, or net banking.",
        "keywords": "pay payment upi fee",
        "category": "billing"
    }
]

digits = [int(d) for d in roll_no[-2:]]

personalized_entries = [
    {
        "question": "how can i contact customer support",
        "answer": "You can contact support through email or the help desk.",
        "keywords": "contact support help",
        "category": categories[digits[0] % 3]
    },
    {
        "question": "where can i find the latest announcements",
        "answer": "Latest announcements are available on the official portal.",
        "keywords": "announcements updates portal",
        "category": categories[digits[1] % 3]
    }
]

df = pd.DataFrame(fixed_entries + personalized_entries)

print("Q4: Add a New Keyword")

# Select one FAQ entry
print("\nSelected FAQ:")
print(df.loc[0, "question"])

print("\nCurrent Keywords:")
print(df.loc[0, "keywords"])

# Ask user for a new keyword
new_keyword = input("\nEnter a new keyword: ").strip()

# Add keyword to selected FAQ
if new_keyword:
    df.loc[0, "keywords"] += " " + new_keyword

print("\nUpdated Keywords:")
print(df.loc[0, "keywords"])

# Save updated DataFrame
filename = f"Assignment_4/{roll_no}_faq_data.csv"

df.to_csv(filename, index=False)

print("\nUpdated FAQ DataFrame:")
print(df.to_string(index=False))

print("\nCSV file saved successfully:", filename)