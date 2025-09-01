"""
    OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class
"""


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


school_bus = Bus("Volvo", 150, 20)
result = isinstance(school_bus, Vehicle)
print(result)
