# Program to find HCF/GCD using the subtraction method

numberA = int(input("Enter first number : "))
numberB = int(input("Enter second number : "))

# Work with positive values only
first = abs(numberA)
second = abs(numberB)

# Handle the case where one number is zero
if first == 0:
    hcf = second
elif second == 0:
    hcf = first
else:
    # Keep subtracting the smaller from the larger until both are equal
    while first != second:
        if first > second:
            first = first - second
        else:
            second = second - first
    hcf = first

print("HCF is : ", hcf)