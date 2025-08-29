"""
    OOP Exercise 5: Define a property that must have the same value for every class instance (object)
    Define a class attribute "color" with a default value white. I.e., Every Vehicle should be white.
"""


class Vehicle:
    color = 'White'

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


class Bus(Vehicle):
    pass


class Car(Vehicle):
    pass


new_car = Vehicle("Honda Civic", 140, 50)
print(f'Color: {new_car.color}, Vehicle name: {new_car.name}, Speed: {new_car.max_speed}, Mileage: {new_car.mileage}')
second_new_car = Car("Toyota Supra", 150, 0)
print(
    f'Color: {second_new_car.color}, Vehicle name: {second_new_car.name}, Speed: {second_new_car.max_speed}, Mileage: {second_new_car.mileage}')
