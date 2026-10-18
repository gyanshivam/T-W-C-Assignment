# 01-binary-search
# Topic: O(log n) and Binary Search
# Binary search always checks the middle and drops half the list.

lockers = [2, 4, 6, 8, 10, 12, 14, 16, 18]

input("Sorted lockers: " + str(lockers) + "   n = 9   Press Enter ")
max_guess = input("Maximum checks to find any locker number? ")
target_value = int(input("Pick a locker number from the list: "))

input("Binary search — check the middle, discard half each round.  Press Enter ")
low_index = 0
high_index = len(lockers) - 1
attempts = 0
while low_index <= high_index:
    middle = (low_index + high_index) // 2
    attempts += 1
    print("  round", attempts, "->  checking", lockers[middle])
    if lockers[middle] == target_value:
        break
    elif lockers[middle] < target_value:
        low_index = middle + 1
    else:
        high_index = middle - 1
print("  found", target_value, "at position", middle + 1, "in", attempts, "steps   your guess:", max_guess, "  ->  O(log n)")

input("Steps grow slowly with n.  Press Enter ")
for size, max_steps in [(9, 4), (100, 7), (1000, 10)]:
    print("  n =", size, "  max steps =", max_steps, "  ->  O(log n)")