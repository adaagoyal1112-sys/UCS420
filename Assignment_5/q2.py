# Assignment 5 - Question 2
# Roll Number: 1024170122

import numpy as np

# Q2(a): Reverse the NumPy array
arr = np.array([1, 2, 3, 6, 4, 5])

print("Q2(a): Reverse the NumPy Array")
print("Original Array:", arr)
print("Reversed Array:", arr[::-1])


# Q2(b): Find the most frequent value and its indices

x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])


def most_frequent(arr):
    values, counts = np.unique(arr, return_counts=True)

    max_count = np.max(counts)

    frequent_values = values[counts == max_count]

    for value in frequent_values:
        indices = np.where(arr == value)[0]

        print("Most Frequent Value:", value)
        print("Frequency:", max_count)
        print("Indices:", indices)


print("\nQ2(b)(i): Array x")
print("Array:", x)
most_frequent(x)

print("\nQ2(b)(ii): Array y")
print("Array:", y)
most_frequent(y)