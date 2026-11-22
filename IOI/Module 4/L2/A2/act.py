# 11-first-set-bit.py
# Topic: position of the rightmost 1-bit (the "first set bit")

print("The first set bit is the RIGHTMOST 1 in a binary number.")
print("Positions are counted from 0 on the right.")
print("To find it: shift right one bit at a time and check the last bit with & 1.")
print("The first time the last bit is 1, we stop - the shift count so far is the position.")
print("--------------------")

# ---------- Section 1 : two demo numbers, both chosen by the user ----------
print("1) Two examples side by side - one with bit 0 set, one with a higher bit.")
o = int(input("   Pick an ODD number   (bit 0 is set, try 5): "))
e = int(input("   Pick an EVEN number  (bit 0 is clear, try 8): "))

input("   Press Enter to walk the bits of the ODD number until the first 1 ")
temp = o
pos = 0
while temp > 0:
    print("      binary:", bin(temp)[2:], "  last bit:", temp & 1)
    if temp & 1:
        break
    pos += 1
    temp >>= 1
print("      first set bit in", o, "is at position", pos)

input("   Press Enter to walk the bits of the EVEN number until the first 1 ")
temp = e
pos = 0
while temp > 0:
    print("      binary:", bin(temp)[2:], "  last bit:", temp & 1)
    if temp & 1:
        break
    pos += 1
    temp >>= 1
print("      first set bit in", e, "is at position", pos)

print("--------------------")

# ---------- Section 2 : your own test, with a guess ----------
print("2) Your turn - pick a number, guess the position, then check.")
n = int(input("   Pick a number (try 8 or 14): "))
guess = input("   Your guess - first set bit at which position? ")
input("   Press Enter to shift " + str(n) + " until the first 1 appears ")
temp = n
pos = 0
while temp > 0:
    print("      binary:", bin(temp)[2:], "  last bit:", temp & 1)
    if temp & 1:
        break
    pos += 1
    temp >>= 1
print("      first set bit in", n, "is at position", pos, "  your guess:", guess)