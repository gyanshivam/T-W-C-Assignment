# 03-list-in-memory.py
# Topic: Space Complexity — how much memory an algorithm uses
# List stores every score in memory, so memory grows as n grows (On space)

n = 4

# Build the list by appending each score in a loop
guess = input("Predict: how many items in the List for n = 4? ")
points = []
for score in range(1, n + 1):
    points.append(score)
print("  your guess:", guess, "  List:", points, "  items:", len(points))

input("Predict: what happens to List size as n grows? Press Enter ")
for size in [4, 10, 100, 1000]:
    scores = []
    for value in range(1, size + 1):
        scores.append(value)
    print(f"n = {size:<5}  List uses {len(scores):>5} items in memory")