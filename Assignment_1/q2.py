import numpy as np

# Q2(a)
array = np.array([[1, -2, 3],
                  [-4, 5, -6]])

print("Q2(a)(i): Absolute Values")
print(np.abs(array))

print("\nQ2(a)(ii): Percentiles")

for p in [25, 50, 75]:
    print(f"\n{p}th Percentile:")
    print("Flattened:", np.percentile(array, p))
    print("Column-wise:", np.percentile(array, p, axis=0))
    print("Row-wise:", np.percentile(array, p, axis=1))

print("\nQ2(a)(iii): Mean")
print("Flattened:", np.mean(array))
print("Column-wise:", np.mean(array, axis=0))
print("Row-wise:", np.mean(array, axis=1))

print("\nMedian")
print("Flattened:", np.median(array))
print("Column-wise:", np.median(array, axis=0))
print("Row-wise:", np.median(array, axis=1))

print("\nStandard Deviation")
print("Flattened:", np.std(array))
print("Column-wise:", np.std(array, axis=0))
print("Row-wise:", np.std(array, axis=1))


# Q2(b)
a = np.array([-1.8, -1.6, -0.5, 0.5, 1.6, 1.8, 3.0])

print("\nQ2(b): Rounding Operations")

print("Original Array:", a)
print("Floor:", np.floor(a))
print("Ceiling:", np.ceil(a))
print("Truncated:", np.trunc(a))
print("Rounded:", np.round(a))