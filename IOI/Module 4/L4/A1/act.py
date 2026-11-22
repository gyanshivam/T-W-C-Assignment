# 07-power-of-2-check.py
# Topic: the n & (n-1) trick - clears the rightmost 1-bit; power-of-2 check

print("Rule:  n & (n-1)  always clears the rightmost 1-bit of n.")
print("       If n is a power of 2, it has exactly ONE 1-bit, so clearing it")
print("       leaves 0  ->  n & (n-1) == 0.")
print("       If n has more than one 1-bit, clearing one leaves others behind.")
print("--------------------")

# ---------- Section 1 : watch one bit get cleared (NOT a power of 2) ----------
print("1) Watch a bit get cleared - on a number that is NOT a power of 2.")
x = int(input("   Pick a non-power-of-2 (try 12): "))
input("   Press Enter to compare " + str(x) + " with " + str(x - 1) + " bit by bit ")
print("      n       =", x, "->", bin(x)[2:])
print("      n - 1   =", x - 1, "->", bin(x - 1)[2:])
print("      n&(n-1) =", x & (x - 1), "->", bin(x & (x - 1))[2:],
      "  (rightmost 1-bit gone, but 1s remain -> not 0)")

print("--------------------")

# ---------- Section 2 : same trick on a power of 2 ----------
print("2) Same trick on a power of 2 - only ONE 1-bit, so the result is 0.")
y = int(input("   Pick a power of 2 (try 8): "))
input("   Press Enter to compare " + str(y) + " with " + str(y - 1) + " bit by bit ")
print("      n       =", y, "->", bin(y)[2:])
print("      n - 1   =", y - 1, "->", bin(y - 1)[2:])
print("      n&(n-1) =", y & (y - 1), "->", bin(y & (y - 1))[2:],
      "  (the only 1-bit was cleared -> 0)")

print("--------------------")

# ---------- Section 3 : your own power-of-2 test ----------
print("3) Put it together:  n > 0  and  (n & (n-1)) == 0  means power of 2.")
n = int(input("   Pick a number to test (try 4 or 6): "))
guess = input("   Your guess - is " + str(n) + " a power of 2? (yes/no): ")
input("   Press Enter to run " + str(n) + " through the rule ")
if n > 0 and (n & (n - 1)) == 0:
    print("      ", n, "->", bin(n)[2:], "  n&(n-1) =", n & (n - 1),
          "  power of 2: yes  your guess:", guess)
else:
    print("      ", n, "->", bin(n)[2:], "  n&(n-1) =", n & (n - 1),
          "  power of 2: no   your guess:", guess)