# ================================
#  NATURAL NUMBERS SUM
#  File: natural-numbers-sum.py
# ================================

# Start from the largest number and count backwards to 1
current = 10
running_total = 0

while current >= 1:
    running_total += current
    current -= 1

print("The sum of the first ten natural numbers is", running_total)