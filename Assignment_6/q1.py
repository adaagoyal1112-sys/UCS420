# Assignment 6 - Question 1
# Roll Number: 1024170122

import numpy as np

temperature = np.array([25, 28, 31, 35, 38, 27, 33, 40])

print("Q1: Sensor Temperature Readings")

print("\nOriginal Temperatures (Celsius):")
print(temperature)

# Q1(a): Add 2°C using vectorization
corrected_temperature = temperature + 2

print("\nQ1(a): Temperatures After Adding 2°C")
print(corrected_temperature)

# Q1(b): Convert Celsius to Fahrenheit
fahrenheit = (corrected_temperature * 9 / 5) + 32

print("\nQ1(b): Temperatures in Fahrenheit")
print(fahrenheit)

# Q1(c): Identify readings greater than 32°C
mask = corrected_temperature > 32

print("\nQ1(c): Boolean Mask for Temperatures > 32°C")
print(mask)

print("\nReadings Greater Than 32°C:")
print(corrected_temperature[mask])

# Q1(d): Count readings exceeding 32°C
count = np.sum(mask)

print("\nQ1(d): Number of Readings Exceeding 32°C")
print(count)

# Q1(e): Explanation
print("\nQ1(e): Explanation")
print("Vectorization performs operations on entire arrays without loops.")
print("Boolean indexing filters elements directly using conditions.")
print("Both improve efficiency and make code shorter and easier to read.")
