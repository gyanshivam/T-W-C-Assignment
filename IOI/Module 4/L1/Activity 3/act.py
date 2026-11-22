# 03-parity-and-bit-count.py
# Topic: parity from the last bit, and counting 1s by shifting one bit at a time

print("This program answers two questions about an integer:")
print("  1) parity    - even or odd?  only the last bit decides.")
print("  2) bit count - how many 1s are in its binary form?")
print("     we shift the number right one bit at a time and count the 1s we drop.")
print("--------------------")

# ---------- PARITY ----------
print("1) Parity   n & 1  gives 0 for even, 1 for odd.")
a = int(input("   First number  (try an even one, like 4): "))
b = int(input("   Second number (try an odd one,  like 9): "))
input("   Press Enter to read the last bit of each ")
for n in [a, b]:
    if n & 1:
        print("      ", n, "->", bin(n)[2:], "  last bit 1 -> odd")
    else:
        print("      ", n, "->", bin(n)[2:], "  last bit 0 -> even")

print("--------------------")

# ---------- BIT COUNT ----------
print("2) Bit count   every right shift drops one bit; count the drops that are 1.")
c = int(input("   Pick a number to count 1s in (try 13 or 7): "))
input("   Press Enter to watch its bits drop off, one at a time ")
temp = c
ones = 0
while temp > 0:
    print("      binary:", bin(temp)[2:], "  last bit:", temp & 1)
    if temp & 1:
        ones += 1
    temp >>= 1
print("      total 1s in", c, "=", ones, "  (cross-check with .count:", bin(c).count('1'), ")")