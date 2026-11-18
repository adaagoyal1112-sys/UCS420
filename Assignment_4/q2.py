# Assignment 4 - Question 2
# Roll Number: 1024170122

import pandas as pd
import re

# FAQ Knowledge Base from Q1
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

categories = ["billing", "account", "general"]
roll_no = "1024170122"
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


# Scoring function
def score_query(query, df):
    query_words = set(re.findall(r"\b\w+\b", query.lower()))
    results = []

    for _, row in df.iterrows():
        keyword_words = set(row["keywords"].lower().split())

        matched_words = query_words.intersection(keyword_words)

        if matched_words:
            confidence = len(matched_words) / len(keyword_words)

            results.append({
                "question": row["question"],
                "answer": row["answer"],
                "category": row["category"],
                "confidence": round(confidence, 2)
            })

    results.sort(key=lambda x: x["confidence"], reverse=True)

    return pd.DataFrame(
        results,
        columns=["question", "answer", "category", "confidence"]
    )


# Take query from user
query = input("Enter your query: ")

matches = score_query(query, df)

print("\nQ2: Matching FAQs Ranked by Confidence")

if matches.empty:
    print("No matching FAQ found.")
else:
    print(matches.to_string(index=False))
    