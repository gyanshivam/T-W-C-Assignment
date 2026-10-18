# 02-best-average-worst
# Topic: Worst, Average and Best Case
# Same list. Steps depend on where the target is.

lockers = [12, 45, 8, 67, 23, 91, 34, 56, 19]
#           1   2  3   4   5   6   7   8   9

input("Lockers: " + str(lockers) + "   n = 9   Linear search — checks left to right.  Press Enter ")

wanted = int(input("Enter a locker number to search for: "))

input("Searching for " + str(wanted) + ".  Press Enter to run ")
checks = 0
for locker in lockers:
    checks += 1
    if locker == wanted:
        break
print("  target =", wanted, "  found at position", checks, "  checks =", checks)

input("Compare with best and worst case.  Press Enter ")
middle = len(lockers) // 2
print("  Best: 1 check -> O(1)   Average:", middle, "checks -> O(n)   Worst: 9 checks -> O(n)   Yours:", checks)

input("All three cases.  Press Enter ")
print("  Best O(1)  Average O(n)  Worst O(n)   ->   Big-O = worst case = O(n).")