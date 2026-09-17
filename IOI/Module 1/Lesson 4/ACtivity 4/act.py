# ================================
#  PRIME NUMBER CHECK
#  File: prime-number.py
# ================================

# Ask the user for a whole number
number = int(input("Enter a number to test: "))

# Assume the number is prime until we find a divisor
is_prime = True

# Numbers 1 and below are never prime
if number <= 1:
    is_prime = False
else:
    # Start checking from 2 up to the square root of the number
    divisor = 2
    while divisor * divisor <= number:
        # If the number divides evenly, it is not prime
        if number % divisor == 0:
            is_prime = False
            break
        divisor += 1

# Print the final result based on the flag
if is_prime:
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")