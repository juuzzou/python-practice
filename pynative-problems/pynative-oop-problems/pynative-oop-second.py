"""
    OOP Exercise 3: Create a child class Bus that will inherit all the variables and methods of the Vehicle class
"""


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    def display(self):
        print(f'Vehicle Name: {self.name}\nSpeed: {self.max_speed}\nMileage: {self.mileage}')


bus = Bus('Volvo', 160, 30)
bus.display()
