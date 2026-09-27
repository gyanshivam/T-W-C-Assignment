# ================================
#  CLASS PLANET
#  File: class_planet.py
# ================================

class Planet:
    # Class variable shared by all planets
    category = "Gas Giant"
    # This print runs once when the class is defined
    print("Behold! A new planet of category", category, "has been discovered.")

# Create an object (instance) of the Planet class
jupiter = Planet()