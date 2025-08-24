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

"""
    Exercise 8: Swap two tuples in Python
"""


def swapTuples(tuple_1, tuple_2):
    tuple_1, tuple_2 = tuple_2, tuple_1
    return tuple_1, tuple_2


tuple1 = (11, 22)
tuple2 = (99, 88)
print(swapTuples(tuple1, tuple2))

"""
    Exercise 9: Copy Specific Elements From Tuple
    Write a program to copy elements 44 and 55 from the following tuple into a new tuple.
"""


def copySpecificElement(tuple_input):
    tuple_output = tuple_input[3:5]
    return tuple_output


tuple1 = (11, 22, 33, 44, 55, 66)
print(copySpecificElement(tuple1))

"""
    Exercise 10: List to Tuple
    Convert a list my_list = [10, 20, 30] into a tuple.
"""


def convertToTuple(list_input):
    tuple_output = tuple(list_input)
    return tuple_output


my_list = [10, 20, 30]
print(convertToTuple(my_list))

"""
    Exercise 11: Function Returning Tuple
    Write a function get_min_max(numbers) that takes a list of numbers and returns a tuple containing the minimum and maximum number.
"""


def getMinMax(list):
    list_min = min(list)
    list_max = max(list)
    return list_min, list_max


my_numbers = [10, 5, 20, 2, 15]
print(getMinMax(my_numbers))

"""
    Exercise 12: Comparing Tuples
    Compare two tuples and find out which one is “greater” and why?
"""


def compareTuples(tuple_1, tuple_2):
    temp_list_1 = list(tuple_1)
    temp_list_2 = list(tuple_2)
    temp_sum_1, temp_sum_2 = sum(temp_list_1), sum(temp_list_2)
    if temp_sum_1 > temp_sum_2:
        print(f'{tuple_1} is greater than {tuple_2}')
    else:
        print(f'{tuple_2} is greater than {tuple_1}')


t1 = (1, 2, 3)
t2 = (1, 2, 4)
compareTuples(t1, t2)

"""
    Exercise 13: Removing Duplicates from Tuple
    Write a code to create a new tuple with only unique elements.
"""


def removeDuplicates(tuple):
    temp_set = set(tuple)
    return_tuple = (temp_set)
    return return_tuple


my_tuple = (1, 2, 2, 3, 4, 4, 5)
print(removeDuplicates(my_tuple))

"""
    Exercise 14: Filter Tuples
    Write a code to filter out students with scores less than 90 from a given a list of tuples.
"""


def filterTuples(input_tuple):
    new_array = []
    for item in input_tuple:
        if item[1] >= 90:
            new_array.append(item)
    return new_array


students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
print(filterTuples(students))

"""
    Exercise 15: Map Tuples
    Given a tuple of numbers, create a new tuple where each number is squared.
"""


def mapTuples(input_tuple):
    return tuple(item ** 2 for item in input_tuple)


t = (1, 2, 3, 4)
print(mapTuples(t))

"""
    Exercise 16: Modify Tuple
    Given is a nested tuple. Write a program to modify the first item (22) of a list inside a following tuple to 222
"""


def modifyTuple(input_tuple):
    input_tuple[1][0] = 222
    return input_tuple


tuple1 = (11, [22, 33], 44, 55)
print(modifyTuple(tuple1))
