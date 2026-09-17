# ================================
#  CALCULATOR - EXTRA OPERATIONS
#  File: calculator_extra_ops.py
# ================================

# This function raises the first number to the power of the second
def power(base, exponent):
    return base ** exponent

# This function gives the remainder after division
def remainder(dividend, divisor):
    return dividend % divisor

# This function performs floor division (whole number quotient)
def floor_divide(dividend, divisor):
    return dividend // divisor

# This function finds the average of two numbers
def average(first, second):
    return (first + second) / 2

# Ask the user for two numbers
value1 = int(input("Enter Number 1: "))
value2 = int(input("Enter Number 2: "))

# Display the results of each operation
print("Power :", power(value1, value2))
print("Remainder :", remainder(value1, value2))
print("Floor Quotient :", floor_divide(value1, value2))
print("Average :", average(value1, value2))