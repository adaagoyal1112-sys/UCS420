# Assignment 5 - Question 4
# Roll Number: 1024170122

import numpy as np

# Create 1D array with 25 evenly spaced numbers
adaa = np.linspace(10, 100, 25)

print("Q4: NumPy Array Using linspace()")

print("\nOriginal Array:")
print(adaa)

# Array properties
print("\nNumber of Dimensions:", adaa.ndim)
print("Shape of Array:", adaa.shape)
print("Total Number of Elements:", adaa.size)
print("Data Type:", adaa.dtype)
print("Total Bytes Consumed:", adaa.nbytes)

# Transpose using reshape()
transposed_adaa = adaa.reshape(25, 1)

print("\nTranspose Using reshape():")
print(transposed_adaa)

print("\nShape After reshape():", transposed_adaa.shape)

# Transpose using T attribute
print("\nTranspose Using T Attribute:")
print(adaa.T)

print("\nShape After T:", adaa.T.shape)

# Conclusion
print("\nConclusion:")
print("For a 1D array, the T attribute does not change its shape.")
print("reshape(25, 1) converts the 1D array into a column vector.")