"""
    Exercise 1: Perform Basic Tuple Operations
        Create a Tuple: Create a tuple named my_tuple containing the numbers 1, 2, 3, 4, and 5.
        Access Elements: Access and print the third element of my_tuple.
        Tuple Length: Find and print the length of my_tuple.
"""


def basicOperations():
    new_tuple = (1, 2, 3, 4, 5)
    print(f'The 3rd element is {new_tuple[2]}')
    print(f'The length of this tuple is {len(new_tuple)}')


basicOperations()

"""
    Exercise 2: Tuple Repetition
    Repeat a below tuple three times.
"""


def repetition():
    original_tuple = ('a', 'b')
    return original_tuple * 3


print(repetition())

"""
    Exercise 3: Slicing Tuples
    Slice below tuple to get elements from the 4th to the 7th position.
"""


def sliceTuple(tuple):
    return tuple[3:7]


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(sliceTuple(numbers))

"""
    Exercise 4: Reverse the tuple
"""


def reverseTuple(tuple):
    return tuple[::-1]


tuple1 = (10, 20, 30, 40, 50)
print(reverseTuple(tuple1))

"""
    Exercise 5: Access Nested Tuples
    Write a code to access and print value 20 from given nested tuple.
"""


def accessNesterTuple(tuple):
    return tuple[1][1]


tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(accessNesterTuple(tuple1))

"""
    Exercise 6: Create a tuple with single item 50
"""


def createATuple():
    tuple_output = (50,)
    return tuple_output


print(createATuple())

"""
    Exercise 7: Unpack the tuple into 4 variables
    Write a code to unpack the following tuple into four variables and display each variable.
"""


def unpackTuple(tuple_input):
    a, b, c, d = tuple_input
    return a, b, c, d


tuple1 = (10, 20, 30, 40)
print(*unpackTuple(tuple1))
