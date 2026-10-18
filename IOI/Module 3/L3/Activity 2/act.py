# 02-recursion
# Topic: Recursion and Recursive Time Complexity
# A function that calls itself. Each call stacks up.

layers = int(input("Enter number of gift layers (try 3 or 5): "))
prediction = input("How many times does unwrap call itself for " + str(layers) + " layers? ")

input("Recursion — watch each call.  Press Enter to run ")
def unwrap(level):
    print("  call — layer =", level)
    if level > 0:
        unwrap(level - 1)
unwrap(layers)
print("  calls =", layers + 1, "  your prediction:", prediction, "  ->  O(n)")

input("Watch calls grow with n.  Press Enter ")
for size in [5, 10, 100]:
    print("  n =", size, "  calls =", size + 1, "  ->  O(n)")