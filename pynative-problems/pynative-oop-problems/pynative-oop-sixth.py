"""
    OOP Exercise 7: Check type of an object
    Write a program to determine which class a given Bus object belongs to.
"""


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


school_bus = Bus("Volvo", 120, 30)
print(type(school_bus))
