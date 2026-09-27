# ================================
#  CLASS CHEF
#  File: class_chef.py
# ================================

class Chef:
    # Class variables shared by every Chef object
    cuisine = "Italian"
    speciality = "Wood-Fired Pizza"

    # First function: prints a simple sentence (no class variables used)
    def welcome(self):
        print("Hello! I am your personal chef today.")

    # Second function: prints the class variables using self
    def profile(self):
        print("I cook", self.cuisine, "food.")
        print("My speciality is", self.speciality)

# Create an object of the Chef class
italian_chef = Chef()

# Call the two functions using the object
italian_chef.welcome()
italian_chef.profile()