# 03-space-complexity
# Topic: Space Complexity and the Complexity Ladder
# Watch O(n) and O(n^2) grow, then see all four on the ladder.

prediction = input("At n = 1000, how many steps does O(n^2) take? ")

input("Compare O(n) and O(n^2) as n grows.  Press Enter ")
for size in [10, 100, 1000]:
    input("n = " + str(size) + "   Press Enter ")
    linear = size
    quadratic = size * size
    print("  O(n) =", linear, "   O(n^2) =", quadratic)

print("  your prediction:", prediction)

input("Build the full ladder at n = 1000.  Press Enter ")
n = 1000

constant = 1

halvings = 0
remaining = n
while remaining > 1:
    remaining = remaining // 2
    halvings += 1

linear = n
quadratic = n * n

print("  O(1) =", constant)
print("  O(log n) =", halvings)
print("  O(n) =", linear)
print("  O(n^2) =", quadratic)