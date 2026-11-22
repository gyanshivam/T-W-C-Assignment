# 08-power-of-4-and-8.py
# Topic: power of 4 via n % 3 == 1, power of 8 via n % 7 == 1

print("Two quick checks, one per section:")
print("  Power of 4:  n > 0  and  n & (n-1) == 0  and  n % 3 == 1")
print("               (one 1-bit, sitting in an even bit position)")
print("  Power of 8:  n % 7 == 1")
print("               (one 1-bit, sitting in a position divisible by 3)")
print("You pick the number in each demo, so you can watch the rule at work.")
print("--------------------")

# ---------- Section 1 : power of 4 ----------
print("1) Power of 4 - three conditions: positive, one 1-bit, and n % 3 == 1.")
p4 = int(input("   Pick a number to test as a power of 4 (try 16): "))
input("   Press Enter to run " + str(p4) + " through the power-of-4 check ")
print("      n       =", p4, "->", bin(p4)[2:])
print("      n - 1   =", p4 - 1, "->", bin(p4 - 1)[2:])
print("      n&(n-1) =", p4 & (p4 - 1), "->", bin(p4 & (p4 - 1))[2:])
print("      n % 3   =", p4 % 3)
if p4 > 0 and (p4 & (p4 - 1)) == 0 and p4 % 3 == 1:
    print("      power of 4: yes")
else:
    print("      power of 4: no")

print("--------------------")

# ---------- Section 2 : power of 8 ----------
print("2) Power of 8 - a simple remainder rule: n % 7 == 1.")
p8 = int(input("   Pick a number to test as a power of 8 (try 8): "))
input("   Press Enter to run " + str(p8) + " through the power-of-8 check ")
print("      n       =", p8, "->", bin(p8)[2:])
print("      n % 7   =", p8 % 7)
if p8 % 7 == 1:
    print("      power of 8: yes")
else:
    print("      power of 8: no")

print("--------------------")

# ---------- Section 3 : your own power-of-4 test with a guess ----------
print("3) Your turn - test your own number for power of 4.")
n = int(input("   Pick a number to test (try 64 or 32): "))
guess = input("   Your guess - is " + str(n) + " a power of 4? (yes/no): ")
input("   Press Enter to check the three conditions on " + str(n) + " ")
is_pow4 = n > 0 and (n & (n - 1)) == 0 and n % 3 == 1
print("      n       =", n, "->", bin(n)[2:])
print("      n&(n-1) =", n & (n - 1), "   n % 3 =", n % 3)
if is_pow4:
    print("      power of 4: yes  your guess:", guess)
else:
    print("      power of 4: no   your guess:", guess)