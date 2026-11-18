L = [70, 40, 20, 20, 20, 10, 10, 10, 0, 0]
scores = tuple(L[:8])

print("Original Tuple:", scores)

# (i) Highest and Lowest Scores
print("\nQ2(i): Highest and Lowest Scores")

highest = max(scores)
lowest = min(scores)

print("Highest Score:", highest)
print("Index of Highest Score:", scores.index(highest))
print("Lowest Score:", lowest)
print("Lowest Score Count:", scores.count(lowest))

# (ii) Reverse Tuple as List
print("\nQ2(ii): Reverse Tuple")

reversed_scores = list(scores[::-1])
print("Reversed List:", reversed_scores)

# Tuples are immutable, so they cannot be reversed in place.

# (iii) Search for a Score
print("\nQ2(iii): Search Score")

score = int(input("Enter a score to search: "))

if score in scores:
    print("First Occurrence Index:", scores.index(score))
else:
    print("Score not present in tuple.")

# (iv) Attempt to Modify Tuple
print("\nQ2(iv): Tuple Immutability")

try:
    scores[0] = 100
except TypeError as e:
    print("Error:", e)

# Tuples are immutable, unlike lists whose elements can be modified.

# (v) Tuple Unpacking
print("\nQ2(v): Tuple Unpacking")

first, second, *remaining = scores

print("First Score:", first)
print("Second Score:", second)
print("Remaining Scores:", remaining)