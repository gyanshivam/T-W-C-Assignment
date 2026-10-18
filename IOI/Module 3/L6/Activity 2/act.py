# Implementation of Sieve of Eratosthenes using a set

def sieve_with_set(limit):
    # Start with every number from 2 to limit as a potential prime
    candidates = set()
    for value in range(2, limit + 1):
        candidates.add(value)

    # For each number still in the set, remove all of its multiples starting from its square
    current = 2
    while current * current <= limit:
        if current in candidates:
            multiple = current * current
            while multiple <= limit:
                if multiple in candidates:
                    candidates.remove(multiple)
                multiple += current
        current += 1

    # Print the remaining numbers in ascending order
    for value in range(2, limit + 1):
        if value in candidates:
            print(value)

num = int(input("Enter a number: "))
print("Following are the prime numbers smaller")
print("than or equal to", num)
sieve_with_set(num)