from abc import ABC, abstractmethod


# ── ABSTRACT BASE CLASS (Parent) ──────────────────────────────────────────────
# Spacecraft inherits from ABC — this makes it an abstract class (Abstraction)
class Spacecraft(ABC):

    # Parent constructor — stores attributes shared by ALL spacecraft
    def __init__(self, name, fuel):
        self.name = name
        self.fuel = fuel

    # Concrete method — all child classes inherit this for free
    def display(self):
        print(f"Craft: {self.name}  |  Fuel: {self.fuel}%")

    # Abstract method — every child class MUST implement this
    @abstractmethod
    def launch(self):
        pass


# ── CHILD CLASS 1 ─────────────────────────────────────────────────────────────
class Rocket(Spacecraft):

    def __init__(self, name, fuel, thrust):
        super().__init__(name, fuel)   # calls Spacecraft's constructor
        self.thrust = thrust

    def launch(self):
        print(f"{self.name} (Thrust: {self.thrust} kN) roars: 3... 2... 1... LIFTOFF!")


# ── CHILD CLASS 2 ─────────────────────────────────────────────────────────────
class Satellite(Spacecraft):

    def __init__(self, name, fuel, orbit):
        super().__init__(name, fuel)
        self.orbit = orbit

    def launch(self):
        print(f"{self.name} deploys into {self.orbit} orbit: Beep... Beep... Signal locked!")


# ── CHILD CLASS 3 ─────────────────────────────────────────────────────────────
class Rover(Spacecraft):

    def __init__(self, name, fuel, planet):
        super().__init__(name, fuel)
        self.planet = planet

    def launch(self):
        print(f"{self.name} (Target: {self.planet}) rolls out: Crunch... Crunch... Wheels engaged!")


# ── CREATE OBJECTS & RUN THE LAUNCH SHOW ──────────────────────────────────────
rocket    = Rocket("Falcon-X",   90, 7600)
satellite = Satellite("Starlink-7", 100, "Low Earth")
rover     = Rover("Perseverance", 80, "Mars")

print("=== Spacecraft Launch Show ===\n")
for craft in [rocket, satellite, rover]:
    craft.display()
    craft.launch()
    print()