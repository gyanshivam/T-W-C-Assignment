# ================================
#  CLASS MAGICIAN
#  File: class_magician.py
# ================================

class Magician:

    # Constructor runs automatically when a Magician object is created
    def __init__(self, name, age):
        self.name = name    # instance variable
        self.age = age      # instance variable

    # Instance method that accepts an extra argument
    def cast(self, spell):
        return "{} casts {}".format(self.name, spell)

    # Instance method with no extra arguments
    def vanish(self):
        return "{} disappears in a puff of smoke".format(self.name)

# Create an instance of the Magician class
merlin = Magician("Merlin", 120)

# Call the instance methods and print their returned values
print(merlin.cast("'Fireball'"))
print(merlin.vanish())