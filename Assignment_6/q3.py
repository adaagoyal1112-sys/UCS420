# Assignment 6 - Question 3
# Roll Number: 1024170122

import numpy as np

# Q3(a): Create original array
original = np.array([1, 2, 3, 4, 5, 6])

print("Q3(a): Original Array")
print(original)


# Q3(b): Create slice from index 1 to 4
subset = original[1:5]

print("\nQ3(b): Subset from Index 1 to 4")
print(subset)


# Q3(c): Modify first element of subset
subset[0] = 999

print("\nQ3(c): After Modifying Subset")
print("Original Array:", original)
print("Subset:", subset)


# Q3(d): Create independent copy
copied_array = original[1:5].copy()

copied_array[0] = 500

print("\nQ3(d): After Modifying Copied Array")
print("Original Array:", original)
print("Copied Array:", copied_array)


# Q3(e): Create 3x4 matrix
matrix = np.arange(1, 13).reshape(3, 4)

print("\nQ3(e): 3x4 Matrix")
print(matrix)


# Q3(f): Indexing and slicing
print("\nQ3(f): Matrix Indexing and Slicing")

print("First Row:")
print(matrix[0, :])

print("Last Row:")
print(matrix[-1, :])

print("Second Column:")
print(matrix[:, 1])

print("Rows 1-2 and Columns 2-3:")
print(matrix[0:2, 1:3])


# Q3(g): Flatten and ravel
flattened = matrix.flatten()
raveled = matrix.ravel()

print("\nQ3(g): Flattened Arrays")

print("Using flatten():")
print(flattened)

print("Using ravel():")
print(raveled)


# Q3(h): Modify ravel array
raveled[0] = 100

print("\nQ3(h): After Modifying ravel() Array")
print("Raveled Array:")
print(raveled)

print("Original Matrix:")
print(matrix)


# Q3(i): Modify flatten array
flattened[1] = 200

print("\nQ3(i): After Modifying flatten() Array")
print("Flattened Array:")
print(flattened)

print("Original Matrix:")
print(matrix)


# Q3(j): Matrix properties
print("\nQ3(j): Matrix Properties")

print("Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)
print("Size:", matrix.size)
print("Data Type:", matrix.dtype)