# ================================
#  CLASS ROBOT
#  File: class_robot.py
# ================================

class Robot:
    # Class variable shared by every Robot object
    category = "Android"

    # __init__ runs automatically when a new Robot is created
    def __init__(self, name, battery):
        self.name = name          # instance variable
        self.battery = battery    # instance variable

# Create two Robot objects with different values
r2d2 = Robot("R2-D2", 85)
c3po = Robot("C-3PO", 60)

# Access the class variable using each object
print(f"{r2d2.name} belongs to the {r2d2.category} category.")
print(f"{c3po.name} also belongs to the {c3po.category} category.")

# Access the instance variables using each object
print(f"{r2d2.name} has {r2d2.battery}% battery left.")
print(f"{c3po.name} has {c3po.battery}% battery left.")