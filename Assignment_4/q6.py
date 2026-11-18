# Assignment 4 - Question 6
# Roll Number: 1024170122

import pandas as pd
import re

# Load updated FAQ dataset from Q4
df = pd.read_csv("Assignment_4/1024170122_faq_data.csv")


def score_query(query, df):
    query_words = set(re.findall(r"\b\w+\b", query.lower()))
    results = []

    for _, row in df.iterrows():
        keywords = set(row["keywords"].lower().split())
        matched = query_words.intersection(keywords)

        if matched:
            confidence = len(matched) / len(keywords)

            results.append({
                "question": row["question"],
                "answer": row["answer"],
                "category": row["category"],
                "confidence": round(confidence, 2)
            })

    return pd.DataFrame(
        results,
        columns=["question", "answer", "category", "confidence"]
    )


def display_best_matches(query, df):
    print("\nQuery:", query)

    matches = score_query(query, df)

    if matches.empty:
        print("No matching FAQ found.")
        return

    highest_score = matches["confidence"].max()

    best_matches = matches[
        matches["confidence"] == highest_score
    ]

    print("\nHighest Confidence:", highest_score)

    if len(best_matches) > 1:
        print("Tie detected! Displaying all equally ranked FAQs:")
    else:
        print("Best Matching FAQ:")

    print(best_matches.to_string(index=False))


# Example 1: Query producing a tie
display_best_matches("fee pay payment upi cost price charge subscription", df)

# Example 2: Query without a tie
display_best_matches("password reset", df)