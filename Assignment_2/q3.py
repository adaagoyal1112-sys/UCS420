import random
from collections import Counter

# Set random seed using roll number
random.seed(1024170122)

# (i) Generate 100 random numbers between 100 and 900
numbers = [random.randint(100, 900) for _ in range(100)]

print("Q3(i): Random Numbers")
print(numbers)

# (ii) Count and print all odd numbers
odd_numbers = [num for num in numbers if num % 2 != 0]

print("\nQ3(ii): Odd Numbers")
print(odd_numbers)
print("Total Odd Numbers:", len(odd_numbers))

# (iii) Count and print all even numbers
even_numbers = [num for num in numbers if num % 2 == 0]

print("\nQ3(iii): Even Numbers")
print(even_numbers)
print("Total Even Numbers:", len(even_numbers))

# (iv) Count and print all prime numbers

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

prime_numbers = [num for num in numbers if is_prime(num)]

print("\nQ3(iv): Prime Numbers")
print(prime_numbers)
print("Total Prime Numbers:", len(prime_numbers))

# (v) Most frequently occurring number
frequency = Counter(numbers)
most_common_number, count = frequency.most_common(1)[0]

print("\nQ3(v): Most Frequent Number")
print("Number:", most_common_number)
print("Frequency:", count)