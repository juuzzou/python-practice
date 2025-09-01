"""
    OOP Exercise 10: Calculate the area of different shapes using OOP
    You have given a Shape class and subclasses Circle  and Square.
    The parent class (Shape) has an area() method.
    Now, Write a OOP code to calculate the area of each shape (each subclass must write its own implementation of area()
    method to calculates its area).
"""


class Shape:
    def area(self):
        raise NotImplementedError('Area method must be implemented by subclasses')


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self, pi=3.14):
        return pi * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


shapes = [Circle(5), Square(7), Circle(3)]
for shape in shapes:
    print(F'The area is {shape.area():.2f}')
