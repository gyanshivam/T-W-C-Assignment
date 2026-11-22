# 12-masks-and-bit-check.py
# Topic: building bit masks with left shift, checking if the Nth bit is ON

print("Two steps, both driven by a bit position you pick:")
print("  1) Build a mask   - 1 shifted LEFT by k puts a single 1 at position k.")
print("  2) Check bit k    - the mask isolates that one bit of a number.")
print("     n & mask  is 0 when the bit is OFF, nonzero when it is ON.")
print("     An equivalent check is  (n >> k) & 1  - shift bit k down to position 0.")
print("--------------------")

# ---------- Section 1 : build masks for positions 0..3 ----------
print("1) Building masks - one 1 at exactly the chosen position.")
for k in range(4):
    mask = 1 << k
    print("      bit", k, "  mask: 1 <<", k, "=", mask, "  binary:", bin(mask)[2:])

print("--------------------")

# ---------- Section 2 : build your own mask at any position ----------
print("2) Build your own mask - pick a position and see the single 1 land there.")
p = int(input("   Pick a bit position (try 2): "))
input("   Press Enter to shift 1 left by " + str(p) + " ")
mask = 1 << p
print("      mask: 1 <<", p, "=", mask, "  binary:", bin(mask)[2:],
      "  (one 1 at position", str(p) + ")")

print("--------------------")

# ---------- Section 3 : check bit q of a number, two equivalent methods ----------
print("3) Check a real number - both methods agree.")
n = int(input("   Pick a number (try 42 or 13): "))
q = int(input("   Pick the bit position to check (try 2): "))
guess = input("   Your guess - is bit " + str(q) + " of " + str(n) + " ON? (yes/no): ")
input("   Press Enter to test bit " + str(q) + " of " + str(n) + " with the mask ")
mask = 1 << q
masked = n & mask
shifted = (n >> q) & 1
print("      n              =", n, "->", bin(n)[2:])
print("      mask 1 <<", q, "   =", mask, "->", bin(mask)[2:])
print("      n & mask       =", masked, "->", bin(masked)[2:], "   (isolates the bit)")
print("      (n >>", q, ") & 1 =", shifted, "     (bit", q, "shifted to position 0)")

if shifted:
    print("      bit", q, "of", n, "is ON   your guess:", guess)
else:
    print("      bit", q, "of", n, "is OFF  your guess:", guess)