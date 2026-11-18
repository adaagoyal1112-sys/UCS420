roll_no = "1024170122"

# Create list by multiplying each digit by 10
L = [int(digit) * 10 for digit in roll_no]

# (i) Print L
print("Q1(i): Original List")
print(L)

# (ii) Append and Insert
print("\nQ1(ii): Append and Insert")

L.append(50)
print("After append(50):", L)
# append() adds an element at the end of the list.

L.insert(2, 80)
print("After insert(2, 80):", L)
# insert() adds an element at the specified index.

# (iii) Remove and Pop
print("\nQ1(iii): Remove and Pop")

L.remove(50)
print("After remove(50):", L)
# remove() deletes the first occurrence of the given value.

L.pop(2)
print("After pop(2):", L)
# pop() deletes the element at the specified index.

# (iv) Sorting
print("\nQ1(iv): Sorting")

L.sort()
print("Ascending Order:", L)

L.sort(reverse=True)
print("Descending Order:", L)

# (v) Slicing
print("\nQ1(v): Slicing")

print("First 3 Elements:", L[:3])
print("Last 3 Elements:", L[-3:])

# (vi) List Comprehension
print("\nQ1(vi): Elements Greater Than Average")

average = sum(L) / len(L)
greater_than_average = [x for x in L if x > average]

print("Average:", average)
print("Elements Greater Than Average:", greater_than_average)