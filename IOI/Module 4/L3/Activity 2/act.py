# 05-find-odd-one.py
# Topic: find the number that appears once, using XOR cancellation

print("Rule: a number XOR-ed with itself gives 0  (x ^ x = 0).")
print("So if we XOR the whole list, every pair cancels and only the")
print("number that appears once survives.  You choose the numbers.")
print("--------------------")

# ---------- Demo 1 : warm-up, three numbers ----------
print("1) Warm-up: a list of three - one number repeated, one unique.")
p = int(input("   Pick the number that appears twice (try 2): "))
o = int(input("   Pick the number that appears once  (try 4): "))
input("   Press Enter to XOR " + str(p) + " ^ " + str(o) + " ^ " + str(p) + " ")
print("      list: [", p, ",", o, ",", p, "]")
print("      bits: ", p, "->", bin(p)[2:], "   ", o, "->", bin(o)[2:], "   ", p, "->", bin(p)[2:])
print("      result:", p ^ o ^ p, "->", bin(p ^ o ^ p)[2:],
      "  (the two", str(p) + "s cancelled,", o, "survived)")

print("--------------------")

# ---------- Demo 2 : five numbers, XOR-ed with a loop ----------
print("2) Longer list: two numbers repeated, one appears only once.")
a = int(input("   First number that repeats  (try 3): "))
b = int(input("   Second number that repeats (try 5): "))
n = int(input("   The number that appears once (try 7 or 11): "))
nums = [a, b, n, a, b]
guess = input("   Your guess - which number in " + str(nums) + " appears once? ")
input("   Press Enter to XOR them one at a time and watch the running result ")
print("      list:", nums)
result = 0
for x in nums:
    result ^= x
    print("        ^", x, "->  running:", result, " ->", bin(result)[2:])
print("      odd-occurring:", result, "  your guess:", guess)