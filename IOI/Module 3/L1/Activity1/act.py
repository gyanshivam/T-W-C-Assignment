# 01-three-algorithms.py
# Topic: Algorithms — three ways to solve the same problem (Formula, Loop, Double Loop)
# Same answer every time, but the number of steps is different

# 5 players in a quiz: player 1 earns 1 pt, player 2 earns 2 pts, ... player 5 earns 5 pts
players = 5

guess = input("Total points: 1 + 2 + 3 + 4 + 5 = ")

input("Method A - Formula: one direct calculation.  Press Enter to run ")
steps_a = 1
total_a = players * (players + 1) // 2
print("  total =", total_a, "  steps =", steps_a)

input("Method B - Single Loop: adds one player at a time.  Press Enter to run ")
steps_b = 0
total_b = 0
for player in range(1, players + 1):
    total_b += player
    steps_b += 1
print("  total =", total_b, "  steps =", steps_b)

input("Method C - Double Loop: counts every single point one by one.  Press Enter to run ")
steps_c = 0
total_c = 0
for player in range(1, players + 1):
    for point in range(1, player + 1):
        total_c += 1
        steps_c += 1
print("  total =", total_c, "  steps =", steps_c, "  your guess was:", guess)