my_dict = {
    "name": "Adaa Goyal",
    "roll_no": "1024170122",
    "branch": "ENC",
    "age": 20,
    "city": "Patiala"
}

print("Original Dictionary:", my_dict)

# (i) Rename city to location
print("\nQ5(i): Rename Key")

my_dict["location"] = my_dict.pop("city")
print("After renaming:", my_dict)

# (ii) Add CGPA
print("\nQ5(ii): Add CGPA")

my_dict["cgpa"] = 7.5
print("After adding CGPA:", my_dict)

# (iii) Increase age by 1
print("\nQ5(iii): Update Age")

my_dict["age"] += 1
print("Updated Age:", my_dict["age"])

# (iv) Delete branch using pop() and del
print("\nQ5(iv): Delete Branch")

dict1 = my_dict.copy()
dict2 = my_dict.copy()

removed_value = dict1.pop("branch")
print("Using pop():", dict1)
print("Removed Value:", removed_value)

del dict2["branch"]
print("Using del:", dict2)

# pop() returns the deleted value, while del does not return anything.

# (v) Iterate using items()
print("\nQ5(v): Dictionary Items")

for key, value in my_dict.items():
    print(f"{key} → {value}")

# (vi) Check if email exists
print("\nQ5(vi): Check Email")

if "email" in my_dict:
    print("Email:", my_dict["email"])
else:
    print("Email key does not exist.")

# (vii) Merge dictionaries
print("\nQ5(vii): Merge Dictionaries")

friend_dict = {
    "name": "Riya Sharma",
    "roll_no": "1024170456",
    "branch": "CSE",
    "age": 20,
    "city": "Delhi"
}

merged_dict = {**my_dict, **friend_dict}
print("Merged Dictionary:", merged_dict)

# When keys overlap, values from the second dictionary win.

# (viii) Dictionary comprehension
print("\nQ5(viii): String Values Only")

string_dict = {
    key: value
    for key, value in my_dict.items()
    if isinstance(value, str)
}

print("Dictionary with String Values:", string_dict)
