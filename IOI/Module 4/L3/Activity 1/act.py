# 04-xor-rules.py
# Topic: the three basic XOR rules - identity with 0, self-cancel, repeated-value cancel

print("Three XOR rules, one demo each.  You pick the number(s) for every demo.")
print("  Rule 1:  x ^ 0 = x        XOR with 0 changes nothing.")
print("  Rule 2:  x ^ x = 0        a value cancels itself.")
print("  Rule 3:  a ^ x ^ a = x    a repeated value cancels out.")
print("--------------------")

# ---------- Rule 1 : XOR with 0 ----------
print("1) XOR with 0 keeps the number unchanged: x ^ 0 = x")
x = int(input("   Pick a number to XOR with 0 (try 5 or 9): "))
input("   Press Enter to XOR it with 0 and compare the bits ")
print("      x    =", x, "->", bin(x)[2:])
print("      0    = 0 ->", bin(0)[2:])
print("      x ^ 0 =", x ^ 0, "->", bin(x ^ 0)[2:], "  (same bits as x)")

print("--------------------")

# ---------- Rule 2 : XOR with itself ----------
print("2) XOR with itself gives 0: x ^ x = 0   (matching bits all become 0)")
y = int(input("   Pick a number to XOR with itself (try 5 or 9): "))
input("   Press Enter to XOR it with itself ")
print("      y    =", y, "->", bin(y)[2:])
print("      y    =", y, "->", bin(y)[2:])
print("      y ^ y =", y ^ y, "->", bin(y ^ y)[2:], "  (every bit cancelled)")

print("--------------------")

# ---------- Rule 3 : repeated value cancels ----------
print("3) A repeated value cancels out: a ^ x ^ a = x")
a = int(input("   Pick the value that appears twice (try 3): "))
z = int(input("   Pick the value in the middle (try 6 or 11): "))
guess = input("   Your guess - what is " + str(a) + " ^ " + str(z) + " ^ " + str(a) + " = ? ")
input("   Press Enter - the two " + str(a) + "s cancel, leaving only " + str(z) + " ")
print("      a      =", a, "->", bin(a)[2:])
print("      x      =", z, "->", bin(z)[2:])
print("      a      =", a, "->", bin(a)[2:])
print("      a^x^a =", a ^ z ^ a, "->", bin(a ^ z ^ a)[2:], "  your guess:", guess)