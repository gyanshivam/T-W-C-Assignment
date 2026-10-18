def find_factors(num):
    factors = []
    divisor = 1
    while divisor <= num:
        if num % divisor == 0:
            factors.append(divisor)
        divisor += 1
    return factors

number = int(input("Enter a number: "))
result = find_factors(number)
print("Factors of", number, "are:", result)