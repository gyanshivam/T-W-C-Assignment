# 09-binary-exponentiation.py
# Topic: binary exponentiation - using the bits of the exponent to compute powers

print("Binary exponentiation reads the exponent's bits from RIGHT to LEFT.")
print("  Start:        result = 1,  base = 2.")
print("  For each bit: multiply result by  base ** bit")
print("                 (bit = 0 -> base**0 = 1, so OFF bits add nothing)")
print("                then square base before moving to the next bit.")
print("Only the ON bits actually multiply in - that's why the method is fast.")
print("--------------------")

# ---------- Section 1 : two known cases ----------
print("1) Two known cases, written as bits of the exponent:")
print("     2^8 = 256    exponent 8 =", bin(8)[2:], "in binary")
print("     2^5 = 32     exponent 5 =", bin(5)[2:], "in binary")

print("--------------------")

# ---------- Section 2 : walk one user-chosen exponent, bit by bit ----------
print("2) Walk it yourself - pick an exponent from 0 to 7,")
print("   so three bit positions are enough to reach 2^exponent.")
exp = int(input("   Enter exponent (try 3 or 6): "))
bits = bin(exp)[2:]
low3 = ('00' + bits)[-3:]     # pad on the LEFT so we always have at least 3 chars
b0 = int(low3[2])             # LSB     (1s place)
b1 = int(low3[1])             # middle  (2s place)
b2 = int(low3[0])             # MSB     (4s place)
print("      exponent", exp, "=", bits, "in binary   (low three bits:", low3 + ")")
guess = input("   Your guess - what is 2^" + str(exp) + "? ")

input("   Press Enter to walk the bits from right to left ")
base = 2
r = 1
print("      start:        result =", r, "   base =", base)
r = r * base ** b0
print("      bit 0 =", b0, " ->  result =", r, "   (base**0 = 1, so an OFF bit adds nothing)")
base = base * base
print("                     base squares to", base)
r = r * base ** b1
print("      bit 1 =", b1, " ->  result =", r)
base = base * base
print("                     base squares to", base)
r = r * base ** b2
print("      bit 2 =", b2, " ->  result =", r)

print("--------------------")

# ---------- Section 3 : cross-check with a direct calculation ----------
print("3) The walkthrough should match a direct calculation.")
print("      direct:      2 ^", exp, "=", 2 ** exp)
print("      walkthrough:      ", r)
print("      your guess:", guess)