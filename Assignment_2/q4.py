roll_no = "1024170122"

# Use the first 8 digits of the roll number
digits = [int(digit) for digit in roll_no[:8]]

# Create sets A and B
A = {digit * 7 for digit in digits}
B = {digit * 9 for digit in digits}

print("Set A:", A)
print("Set B:", B)

# (vi) Union
print("\nQ4(vi): Union")
print("A union B:", A.union(B))

# (vii) Intersection
print("\nQ4(vii): Intersection")
print("A intersection B:", A.intersection(B))

# (viii) Difference
print("\nQ4(viii): Difference")
print("A - B:", A.difference(B))
print("B - A:", B.difference(A))

# difference() returns elements in one set but not the other.
# symmetric_difference() returns elements exclusive to either set.

# (ix) Symmetric Difference
print("\nQ4(ix): Symmetric Difference")
print("A symmetric difference B:", A.symmetric_difference(B))

# (x) Subset and Superset
print("\nQ4(x): Subset and Superset")
print("Is A a subset of B?", A.issubset(B))
print("Is B a superset of A?", B.issuperset(A))

# (xi) Remove an element using discard()
print("\nQ4(xi): Discard Element")

X = int(input("Enter a value to remove from Set A: "))

A.discard(X)
print("Set A after discard:", A)

# discard() does not raise an error if the element is absent,
# whereas remove() raises a KeyError.