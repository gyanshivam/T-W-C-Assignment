# 02-steps-at-scale.py
# Topic: Time Complexity — how steps grow as n gets bigger
# Double Loop at n = 4 took 10 steps. Watch what happens as n grows.

input("Double Loop at n = 4 took 10 steps.  Watch it grow.  Press Enter ")
for n in [10, 100, 1000]:
    input("n = " + str(n) + "   Press Enter ")
    total = 0
    step = 1
    while step <= n:
        total = total + step
        step = step + 1
    print("  steps =", total)