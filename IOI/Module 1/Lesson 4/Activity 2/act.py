# ================================
#  STAR PATTERN (INVERTED TRIANGLE)
#  File: star-pattern.py
# ================================

# Ask the user for the number of rows
rows = int(input("Enter the number of rows: "))

# Outer loop: starts from the total rows and counts down to 1
for i in range(rows, 0, -1):
    # Inner loop: prints 'i' stars on the current row
    for j in range(i):
        print('*', end=' ')
    # Move to the next line after printing all stars in the row
    print()