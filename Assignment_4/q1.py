import pandas as pd

roll_no = "1024170122"

# Four fixed FAQ entries
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

# Categories based on roll number digits
categories = ["billing", "account", "general"]

last_two_digits = [int(d) for d in roll_no[-2:]]

# Two personalized FAQ entries
personalized_entries = [
    {
        "question": "how can i contact customer support",
        "answer": "You can contact support through email or the help desk.",
        "keywords": "contact support help",
        "category": categories[last_two_digits[0] % 3]
    },
    {
        "question": "where can i find the latest announcements",
        "answer": "Latest announcements are available on the official portal.",
        "keywords": "announcements updates portal",
        "category": categories[last_two_digits[1] % 3]
    }
]

# Combine all entries
all_entries = fixed_entries + personalized_entries

# Create DataFrame
df = pd.DataFrame(all_entries)

print("Assignment 4 - Q1: Personalized FAQ Knowledge Base")
print(df.to_string(index=False))

print("\nTotal FAQ Entries:", len(df))