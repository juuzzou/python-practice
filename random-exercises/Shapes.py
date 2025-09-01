"""
    1. Circle Class for Area and Perimeter
    Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
"""


class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius, pi=3.14):
        self.radius = radius
        self.pi = pi

    def area(self):
        return self.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * self.pi * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return self.side * 2


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimeter(self):
        return (self.length + self.width) * 2


def main():
    shapes = [Circle(3), Square(4), Rectangle(3, 4)]
    for shape in shapes:
        print(
            f'The area of this {shape.__class__.__name__} is {shape.area()}\nThe perimeter of this {shape.__class__.__name__} is {shape.perimeter()}')


if __name__ == '__main__':
    main()
