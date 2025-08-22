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

