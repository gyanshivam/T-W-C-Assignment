# 02-bitwise-operators.py
# Topic: NOT, XOR, left shift, right shift - one demo per operator,
#        and the user picks the number(s) for every demo.

print("This program shows four bitwise operators.")
print("For each one you choose the number(s); the program shows the bits.")
print("--------------------")

# ---------- NOT ----------
print("1) NOT  ~x   flips every bit: 0 becomes 1 and 1 becomes 0.")
n = int(input("   Pick a number from 0 to 255 to flip (try 12): "))
input("   Press Enter to flip its bits ")
print("      x  =", n, "->", bin(n)[2:])
print("     ~x  =", ~n, "  full value")
print("      in 8 bits:", bin(~n & 0xFF)[2:], "->", ~n & 0xFF)

print("--------------------")

# ---------- XOR ----------
print("2) XOR  a ^ b   gives 1 where the two numbers differ, 0 where they match.")
a = int(input("   First number  (try 12): "))
b = int(input("   Second number (try 10): "))
input("   Press Enter to compare their bits ")
print("      a  =", a, "->", bin(a)[2:])
print("      b  =", b, "->", bin(b)[2:])
print("     a^b =", a ^ b, "->", bin(a ^ b)[2:])

print("--------------------")

# ---------- SHIFTS ----------
print("3) Left shift  x << 1  doubles x.   Right shift  x >> 1  halves it")
print("   (an odd number rounds down when shifted right).")
s = int(input("   Pick a number to shift (try 5 or 12): "))
guess = input("   Guess " + str(s) + " << 1 = ")
input("   Press Enter to shift left by one ")
print("      ", s, "<< 1 =", s << 1, "->", bin(s << 1)[2:], "  your guess:", guess)
input("   Press Enter to shift right by one ")
print("      ", s, ">> 1 =", s >> 1, "->", bin(s >> 1)[2:])