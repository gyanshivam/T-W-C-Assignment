# Program to check if given number is prime or not

from math import sqrt

number = int(input("Enter your number : "))
print("\n")

# Numbers less than 2 are never prime
if number < 2:
    print(number, "is not a prime number")
else:
    # Try divisors starting from 2 up to the square root of the number
    limit = int(sqrt(number))
    divisor = 2
    has_factor = False

    while divisor <= limit:
        if number % divisor == 0:
            has_factor = True
            break
        divisor += 1

    # If no divisor was found, the number is prime
    if has_factor:
        print(number, "is not a prime number")
    else:
        print(number, "is a prime number")