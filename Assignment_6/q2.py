# Assignment 6 - Question 2
# Roll Number: 1024170122

import numpy as np

# Daily steps of 4 users over 3 days
steps = np.array([
    [5000, 6200, 7100],
    [8000, 7500, 9000],
    [4500, 5100, 4800],
    [9000, 8500, 9500]
])

print("Q2: Daily Step Count Analysis")

print("\nOriginal Steps Matrix:")
print(steps)

# Q2(a): Total steps recorded
print("\nQ2(a): Total Steps Recorded")
print(np.sum(steps))

# Q2(b): Mean number of steps
print("\nQ2(b): Mean Number of Steps")
print(np.mean(steps))

# Q2(c): Maximum and minimum steps
print("\nQ2(c): Maximum and Minimum Steps")
print("Maximum:", np.max(steps))
print("Minimum:", np.min(steps))

# Q2(d): Total steps for each day (axis=0)
print("\nQ2(d): Total Steps for Each Day")
print(np.sum(steps, axis=0))

# Q2(e): Total steps for each user (axis=1)
print("\nQ2(e): Total Steps for Each User")
print(np.sum(steps, axis=1))

# Q2(f): Position of maximum steps using argmax()
max_index = np.argmax(steps)

row, col = np.unravel_index(max_index, steps.shape)

print("\nQ2(f): Position of Maximum Steps")
print("Maximum Steps:", steps[row, col])
print("Row Index:", row)
print("Column Index:", col)
print("User Number:", row + 1)
print("Day Number:", col + 1)