# 06-split-with-xor.py
# Topic: two odd-occurring numbers, split by the rightmost set bit

print("Rule: XOR-ing the whole list cancels every pair, leaving only a ^ b")
print("      (the two numbers that appeared once, still merged together).")
print("To separate them, look at the rightmost set bit of a ^ b: that bit is")
print("ON in exactly one of a, b and OFF in the other - so we split by it.")
print("For this demo pick one ODD and one EVEN survivor, so the split bit")
print("lands on bit 0 (the simplest case).")
print("--------------------")

# ---------- Demo 1 : XOR the list, pairs cancel ----------
print("1) XOR the whole list - every pair cancels, only a ^ b is left over.")
a = int(input("   First survivor, an ODD number  (try 1 or 3): "))
p = int(input("   Value that repeats twice       (try 3): "))
b = int(input("   Second survivor, an EVEN number (try 4): "))
input("   Press Enter to XOR " + str(a) + " ^ " + str(p) + " ^ " + str(b) + " ^ " + str(p) + " ")
xor = a ^ p ^ b ^ p
print("      list: [", a, ",", p, ",", b, ",", p, "]")
print("      bits:  ", a, "->", bin(a)[2:], "   ", p, "->", bin(p)[2:],
      "   ", b, "->", bin(b)[2:], "   ", p, "->", bin(p)[2:])
print("      XOR of all:", xor, "->", bin(xor)[2:],
      "  (the two", str(p) + "s cancelled)")

print("--------------------")

# ---------- Demo 2 : locate the split bit ----------
print("2) Split key - the rightmost set bit of the XOR result is",
      xor & 1, "(bit 0), so we split by bit 0.")
input("   Press Enter to look at bit 0 of the XOR result ")
print("      ", xor, "->", bin(xor)[2:], "  rightmost set bit: bit 0 =", xor & 1,
      "  -> split key is bit 0")

print("--------------------")

# ---------- Demo 3 : split the survivors into groups ----------
print("3) Split - bit 0 ON goes to group A, bit 0 OFF goes to group B.")
guess = input("   Your guess - is bit 0 of " + str(a) + " ON? (yes/no): ")
input("   Press Enter to read bit 0 of each survivor ")
if a & 1:
    print("      ", a, "->", bin(a)[2:], "  bit 0 ON  -> group A  your guess:", guess)
else:
    print("      ", a, "->", bin(a)[2:], "  bit 0 OFF -> group B  your guess:", guess)
if b & 1:
    print("      ", b, "->", bin(b)[2:], "  bit 0 ON  -> group A")
else:
    print("      ", b, "->", bin(b)[2:], "  bit 0 OFF -> group B")
print("      the two odd-occurring numbers are", a, "and", b)