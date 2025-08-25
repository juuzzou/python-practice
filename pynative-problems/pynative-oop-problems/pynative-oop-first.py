"""
    OOP Exercise 1: Create a Class with instance attributes
    Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
"""


class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


new_car = Vehicle(160, 5000)
print(f'My rented has maximum speed of {new_car.max_speed} mi/h and mileage of {new_car.mileage} mi.')

"""
    OOP Exercise 2: Create a Vehicle class without any variables and methods
"""


class AnotherVehicle:
    pass
