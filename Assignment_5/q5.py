# Assignment 5 - Question 5
# Roll Number: 1024170122

import numpy as np

# Create a 2D NumPy array (3 rows and 4 columns)
ucs420_adaa = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 15, 20, 35]
])

print("Q5: NumPy Array Operations")

print("\nOriginal Array:")
print(ucs420_adaa)

print("\nShape:", ucs420_adaa.shape)

# Statistical operations
print("\nMean:", np.mean(ucs420_adaa))
print("Median:", np.median(ucs420_adaa))
print("Maximum:", np.max(ucs420_adaa))
print("Minimum:", np.min(ucs420_adaa))
print("Unique Elements:", np.unique(ucs420_adaa))

# Reshape into 4 rows and 3 columns
reshaped_ucs420_adaa = ucs420_adaa.reshape(4, 3)

print("\nReshaped Array (4 x 3):")
print(reshaped_ucs420_adaa)

print("\nReshaped Array Shape:", reshaped_ucs420_adaa.shape)

# Resize into 2 rows and 3 columns
resized_ucs420_adaa = np.resize(ucs420_adaa, (2, 3))

print("\nResized Array (2 x 3):")
print(resized_ucs420_adaa)

print("\nResized Array Shape:", resized_ucs420_adaa.shape)