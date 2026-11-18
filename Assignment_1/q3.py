import numpy as np

# Q3(a): Searching and Sorting

array = np.array([10, 52, 62, 16, 16, 54, 453])

print("Q3(a): Searching and Sorting")
print("Original Array:", array)

# (i) Sorted Array
print("\nSorted Array:")
print(np.sort(array))

# (ii) Indices of Sorted Array
print("\nIndices of Sorted Array:")
print(np.argsort(array))

# (iii) Four Smallest Elements
print("\nFour Smallest Elements:")
print(np.sort(array)[:4])

# (iv) Five Largest Elements
print("\nFive Largest Elements:")
print(np.sort(array)[-5:][::-1])


# Q3(b): Integer and Float Elements

array = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])

print("\nQ3(b): Integer and Float Elements")
print("Original Array:", array)

# (i) Integer Elements
print("\nInteger Elements:")
print(array[array == np.floor(array)])

# (ii) Non-Integer Elements
print("\nFloat Elements:")
print(array[array != np.floor(array)])