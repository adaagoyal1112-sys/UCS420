# Assignment 4 - Question 3
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


# Function to return questions belonging to a category
def same_category(category_name, df):
    return df.loc[
        df["category"] == category_name,
        "question"
    ]


# Use the category of a personalized FAQ
selected_category = personalized_entries[0]["category"]

print("Q3: FAQs Belonging to the Same Category")
print("Selected Category:", selected_category)

print("\nMatching Questions:")
print(same_category(selected_category, df).to_string(index=False))