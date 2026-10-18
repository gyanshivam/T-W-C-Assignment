# 03-classify-new-algorithm
# Topic: Classify a New Algorithm
# Count the loops. That tells you the Big-O.

size = int(input("Enter any size (try 6, 12, or 40): "))

input("Single loop — runs once per item.  Press Enter to run ")
count = 0
for step in range(size):
    count += 1
print("  size =", size, "  steps =", count, "  ->  O(n)  linear time")

input("Two nested loops — runs size x size times.  Press Enter to run ")
count = 0
for outer in range(size):
    for inner in range(size):
        count += 1
print("  size =", size, "  steps =", count, "  ->  O(n^2)  quadratic time")

input("Rule: count the loops.  Press Enter ")
print("  no loop -> O(1)   one loop -> O(n)   two nested -> O(n^2)")