# Find all palindromic prime numbers up to 3000 using the Sieve of Eratosthenes
# and a string-based palindrome check.

def find_palindromic_primes(limit):
    # Build a sieve: True means "assumed prime" for now
    is_prime = []
    for value in range(limit + 1):
        is_prime.append(True)

    # 0 and 1 are not prime
    is_prime[0] = False
    is_prime[1] = False

    # Mark all multiples of each prime as non-prime
    current = 2
    while current * current <= limit:
        if is_prime[current]:
            multiple = current * current
            while multiple <= limit:
                is_prime[multiple] = False
                multiple += current
        current += 1

    # Collect numbers that are prime AND read the same forwards and backwards
    for candidate in range(2, limit + 1):
        if is_prime[candidate]:
            text = str(candidate)
            if text == text[::-1]:
                print(candidate)

find_palindromic_primes(3000)