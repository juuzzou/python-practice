"""
    Exercise 1: Create a function in Python
    Write a program to create a function that takes two arguments, name and age, and prints their values.
"""

def printAbout(name, age):
    return print(f'Name: {name}; Age: {age}')

printAbout('Wyatt', 22)

"""
    Exercise 2: Create a function with variable length of arguments
    Write a program to create a function func1() that accepts a variable number of arguments and prints each of their values.
"""
def printValue(*args):
    return print(*args)

printValue(10, 20, 30)

"""
    Exercise 3: Return multiple values from a function
    Write a function calculation() that accepts two variables and calculates both their addition and subtraction. 
    The function should then return both the sum and the difference in a single return statement.
"""

def calculation(a, b):
    return a + b, a - b

result = calculation(40, 10)
print(*result)

"""
    Exercise 4: Create a function with a default argument
    Write a program to create a function show_employee() with the following specifications:
        It should accept the employee’s name and salary.
        It should display both the name and salary.
        If the salary is not provided in the function call, it should default to 9000.
"""

def show_employee(name, salary=9000):
    return print(f'Name: {name}\nSalary: {salary}')

show_employee('Wyatt', 6000)
show_employee('Alfajer')

"""
    Exercise 5: Create an inner function
    Create a program with nested functions to perform an addition calculation as follows:
        Define an outer function that accepts two parameters, a and b.
        Inside this outer function, define an inner function that calculates the sum of a and b.
        The outer function should then add 5 to this sum.
        Finally, the outer function should return the resulting value.

"""

def outerFunction(a, b):
    def innerFunction():
        return a + b
    return innerFunction() + 5

print(outerFunction(5, 10))