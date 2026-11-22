# 01-set-and-zero.py
# Topic: Setting bits with OR, clearing bits with AND, power-of-2 check

input("SET a bit: OR forces a bit ON.  Press Enter ")
start = 9
add = 4
print("  start  ", start, "->", bin(start)[2:])
print("  OR ", add, " ->", start | add, "->", bin(start | add)[2:])

input("ZERO a bit: AND forces a bit OFF.  Press Enter ")
now = 13
mask = 9
print("  start  ", now, "->", bin(now)[2:])
print("  AND", mask, " ->", now & mask, "->", bin(now & mask)[2:])

n = int(input("Pick a number (4 and 6 give different answers): "))
guess = input("Your guess - power of 2? (yes/no): ")
input("Check the pattern: a power of 2 has exactly one bit ON.  Press Enter ")

if n > 0 and (n & (n - 1)) == 0:
    verdict = "power of 2"
else:
    verdict = "not a power of 2"

print("  ", n, "->", bin(n)[2:], "->", verdict, "| your guess:", guess)