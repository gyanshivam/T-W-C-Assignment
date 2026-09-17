# ================================
#  FACTORIAL USING RECURSION
#  File: factorial_recursion.py
# ================================

# Define a recursive function to compute factorial
def factorial_recursive(value):
    # Base case: factorial of 0 or 1 is 1
    if value <= 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    return value * factorial_recursive(value - 1)

# Ask the user for a number
number = int(input("Enter a number to find its factorial: "))

# Factorial is not defined for negative numbers
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Call the recursive function and display the result
    result = factorial_recursive(number)
    print(f"The factorial of {number} is {result}")