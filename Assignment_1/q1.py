import numpy as np
from itertools import product

# Q1(a) - Reverse Array

arr = np.array([1, 2, 3, 6, 4, 5])
print("Q1(a):", arr[::-1])


# Q1(b) - Flatten Array

array1 = np.array([[1, 2, 3],
                   [2, 4, 5],
                   [1, 2, 3]])

print("Q1(b):", array1.flatten())


# Q1(c) - Compare Arrays

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[1, 2], [3, 4]])

print("Q1(c):", np.array_equal(arr1, arr2))


# Q1(d): Most Frequent Value and Its Indices
import numpy as np

x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])

for arr in [x, y]:
    values, counts = np.unique(arr, return_counts=True)

    max_count = np.max(counts)
    frequent_values = values[counts == max_count]

    print("Array:", arr)
    print("Most Frequent Values:", frequent_values)
    print("Frequency:", max_count)

    for value in frequent_values:
        print("Indices:", np.where(arr == value)[0])

    print()

    # Q1(e): Matrix Sum
    import numpy as np

gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')

print("Matrix:\n", gfg)

print("Sum of All Elements:", np.sum(gfg))
print("Row-wise Sum:\n", np.sum(gfg, axis=1))
print("Column-wise Sum:", np.sum(gfg, axis=0))

# Q1(f): Matrix Operations
import numpy as np

n_array = np.array([[55, 25, 15],
                    [30, 44, 2],
                    [11, 45, 77]])

print("Matrix:\n", n_array)

print("\nSum of Diagonal Elements:")
print(np.trace(n_array))

eigenvalues, eigenvectors = np.linalg.eig(n_array)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

print("\nInverse:")
print(np.linalg.inv(n_array))

print("\nDeterminant:")
print(np.linalg.det(n_array))

# Q1(g): Matrix Multiplication and Covariance
import numpy as np

# Part i
p1 = np.array([[1, 2],
               [2, 3]])

q1 = np.array([[4, 5],
               [6, 7]])

print("Part i")

print("Matrix Multiplication:\n", np.matmul(p1, q1))
print("Covariance:\n", np.cov(p1, q1))

# Part ii
p2 = np.array([[1, 2],
               [2, 3],
               [4, 5]])

q2 = np.array([[4, 5, 1],
               [6, 7, 2]])

print("\nPart ii")

print("Matrix Multiplication:\n", np.matmul(p2, q2))

# Covariance between corresponding flattened elements
# Both matrices have 6 elements.
print("Covariance:\n",
      np.cov(p2.flatten(), q2.flatten()))

# Q1(h): Inner, Outer and Cartesian Products
import numpy as np
from itertools import product

x = np.array([[2, 3, 4],
              [3, 2, 9]])

y = np.array([[1, 5, 0],
              [5, 10, 3]])

print("Inner Product:\n", np.inner(x, y))

print("\nOuter Product:\n", np.outer(x, y))

print("\nCartesian Product:")
cartesian = list(product(x.flatten(), y.flatten()))
print(cartesian)

