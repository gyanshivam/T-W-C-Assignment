# 10-binary-basics.py
# Topic: decimal -> binary, then the AND and OR bitwise operators

print("Three steps, one per section.  You pick the number(s) for each step.")
print("  1) Convert a decimal number to binary.")
print("  2) AND  - the result has a 1 only where BOTH inputs have a 1.")
print("  3) OR   - the result has a 1 where EITHER input has a 1.")
print("--------------------")

# ---------- Section 1 : decimal -> binary ----------
print("1) Decimal to binary - bin(n)[2:] drops the '0b' prefix and shows the bits.")
n = int(input("   Pick a number to convert (try 5 or 12): "))
guess = input("   Your guess - what is " + str(n) + " in binary? ")
input("   Press Enter to convert " + str(n) + " to binary ")
print("      decimal", n, "->  binary", bin(n)[2:])
print("      your guess:", guess)

print("--------------------")

# ---------- Section 2 : AND ----------
print("2) AND - both bits must be 1:  1 & 1 = 1,  otherwise 0.")
a = int(input("   First number  (try 12): "))
b = int(input("   Second number (try 10): "))
input("   Press Enter to AND " + str(a) + " with " + str(b) + " bit by bit ")
print("      a     =", a, "->", bin(a)[2:])
print("      b     =", b, "->", bin(b)[2:])
print("      a & b =", a & b, "->", bin(a & b)[2:],
      "  (a 1 only where both a and b had a 1)")

print("--------------------")

# ---------- Section 3 : OR ----------
print("3) OR - at least one bit must be 1:  1 | 1 = 1,  1 | 0 = 1,  0 | 0 = 0.")
c = int(input("   First number  (try 12): "))
d = int(input("   Second number (try 10): "))
input("   Press Enter to OR " + str(c) + " with " + str(d) + " bit by bit ")
print("      c     =", c, "->", bin(c)[2:])
print("      d     =", d, "->", bin(d)[2:])
print("      c | d =", c | d, "->", bin(c | d)[2:],
      "  (a 1 wherever either c or d had a 1)")

print("--------------------")