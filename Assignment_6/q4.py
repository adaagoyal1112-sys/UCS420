# Assignment 6 - Question 4
# Roll Number: 1024170122

import numpy as np

# Given feature matrix
X = np.array([
    [6, 70, 3],
    [5, 50, 6],
    [8, 80, 2],
    [4, 30, 8]
])

# Given assistance scores
y = np.array([40, 65, 30, 85])

print("Q4: Ordinary Least Squares Regression")

print("\nFeature Matrix X:")
print(X)

print("\nAssistance Scores y:")
print(y)

# Q4(a): Shape and dimensions
print("\nQ4(a): Shape and Dimensions")
print("Shape:", X.shape)
print("Dimensions:", X.ndim)

# Q4(b): Transpose
XT = X.T

print("\nQ4(b): Transpose of X")
print(XT)

print("\nExplanation:")
print("Rows of X.T represent features, and columns represent users.")

# Q4(c): Matrix multiplication
XTX = XT @ X

print("\nQ4(c): X.T @ X")
print(XTX)

# Q4(d): Matrix inverse
XTX_inv = np.linalg.inv(XTX)

print("\nQ4(d): Inverse of X.T @ X")
print(XTX_inv)

# Q4(e): Ordinary Least Squares coefficients
beta = XTX_inv @ XT @ y

print("\nQ4(e): Regression Coefficients")
print(beta)

# Q4(f): Interpretation
print("\nQ4(f): Interpretation of Coefficients")
print("Beta 1: Contribution of sleep hours to assistance score.")
print("Beta 2: Contribution of activity level to assistance score.")
print("Beta 3: Contribution of stress level to assistance score.")
print("Each coefficient represents the estimated change in score")
print("for a one-unit increase in that feature, holding others constant.")

# Q4(g): Predict assistance score for new user
new_user = np.array([5, 40, 7])

predicted_score = new_user @ beta

print("\nQ4(g): Prediction for New User")
print("New User Features:", new_user)
print("Predicted Assistance Score:", predicted_score)