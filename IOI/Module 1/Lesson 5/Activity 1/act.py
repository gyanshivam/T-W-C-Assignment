# ================================
#  GREETING FUNCTION
#  File: greeting_function.py
# ================================

# Define a function that accepts a name as a parameter
def greet_person(person):
    # Print a friendly introduction using the provided name
    print("Hi there, " + person + "! Welcome aboard.")

# Ask the user to enter their name
name = input("Please enter your name: ")

# Call the function and pass the user's name as an argument
greet_person(name)