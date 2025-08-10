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
show_employee('Jon Snow')

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

"""
    Exercise 6: Create a recursive function
    Write a program to create a recursive function that calculates the sum of numbers from 0 to 10.
    A recursive function is a function that calls itself repeatedly.
"""

def addition(value):
    if value == 1:
        return value
    return value + addition(value - 1)
print(addition(10))

"""
    Exercise 7: Assign a different name to function and call it through the new name
    Below is the function display_student(name, age). 
    Assign a new name show_student(name, age) to it and call it using the new name.
"""
def display_student(name, age):
    print(name, age)

display_student("Emma", 26)
show_students = display_student
show_students('Wyatt', 22)

"""
    Exercise 8: Generate a Python list of all the even numbers between 4 to 30
"""

def generateEvenNumbers():
    _array = []
    for element in range(4, 30, 2):
        _array.append(element)
    return _array

print(generateEvenNumbers())

"""
    Exercise 9: Find the largest item from list
"""

def findLargest(array):
    _largest = 0
    for element in array:
        if element > _largest:
            _largest = element
    return print(_largest)

x = [4, 6, 8, 24, 12, 2]
findLargest(x)

"""
    Exercise 10: Call Function using both positional and keyword arguments
    Define a function describe_pet(animal_type, pet_name) that prints a description of a pet. 
    Call this function using both positional and keyword arguments.
"""

def describePet(animal_type, pet_name):
    return print(f'Animal type: {animal_type}\nPet name: {pet_name}')

describePet(animal_type='Dog', pet_name='Pibble')

"""
    Exercise 11: Create a function with keyword arguments
    The exercise requires you to create a function that can accept any number of keyword arguments. 
    A keyword argument is where you specify the name of the argument along with its value (e.g., name="Alice", age=30). 
    Inside the function, you need to access these arguments and print them in a key-value format.
    Create a function print_info(**kwargs) that accepts keyword arguments and prints the key-value pairs. Call it with different keyword arguments
"""

def printInfo(**kwargs):
    if kwargs:
        for key, value in kwargs.items():
            print(f'{key}: {value}')
    else:
        return None
printInfo(name='Wyatt', age=22)
printInfo(position='Data Engineer', salary='8000')

"""
    Exercise 12: Modifies global variable
    Define a global variable global_var = 10. Write a function that modifies a global variable value.
"""

test_variable = 10

def changeValue():
    global test_variable
    test_variable = 20
    print(test_variable)

print(test_variable)
changeValue()

"""
    Exercise 13: Write a recursive function to calculate the factorial
    Write a recursive function to calculate the factorial of a non-negative integer.
"""

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))

"""
    Exercise 14: Create a lambda function that squares a given number lambda function in Python is a small anonymous function defined using the lambda keyword. 
    The syntax is lambda arguments: expression. The expression is evaluated and returned.
"""

square = lambda x : x ** 2
n = 4
number = square(n)
print(f'The square of {n} is {number}!')