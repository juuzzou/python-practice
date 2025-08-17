"""
    Exercise 1: Perform Basic List Operations

    Perform following operations on given list:
    Access Elements: Print the third element.
    List Length: Print the number of elements in the list
    Check if Empty: Write a code to check is list empty.

"""


def newFunction(list):
    print(f'Initial list: {list}')
    print(f'Third item: {list[2]}')
    print(f'Length of the list: {len(list)}')
    if len(list) == 0:
        print(f'List is empty')
    else:
        print(f'List is not empty')


my_list = [10, 20, 30, 40, 50]
newFunction(my_list)

"""
    Exercise 2: Perform List Manipulation
    Perform following list manipulation operations on given list:
    Change Element: Change the second element of a list to 200 and print the updated list.
    Append Element: Add 600 o the end of a list and print the new list.
    Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
    Remove Element (by value): Remove 600 from the list and print the list.
    Remove Element (by index): Remove the element at index 0 from the list print the list.
"""


def listManipulation(list):
    print(f'Initial list: {list}')
    list[1] = 200
    print(f'After changing second element: {list}')
    list.append(600)
    print(f'List after appending 600: {list}')
    list.insert(2, 300)
    print(f'List after inserting 300 at index 2: {list}')
    list.remove(600)
    print(f'List after removing 600 (by value): {list}')
    list.pop(0)
    print(f'List after removing element at index 0: {list}')


my_list = [10, 20, 30, 40, 50]
listManipulation(my_list)

"""
    Exercise 3: Sum and average of all numbers in a list
    Calculate and print the sum and average of all numbers in a list.
"""


def findSumAndAvg(list):
    print(f'Sum: {sum(list)}\nAvg: {sum(list) / len(list)}')


my_list = [10, 20, 30, 40, 50]
findSumAndAvg(my_list)

"""
    Exercise 4: Reverse a list
"""


def reverseList(list):
    return list[::-1]


list1 = [100, 200, 300, 400, 500]
print(reverseList(list1))

"""
    Exercise 5: Turn every item of a list into its square
    Given a list of numbers. write a program to turn every item of a list into its square.
"""


def squareList(list):
    return [i ** 2 for i in list]


numbers = [1, 2, 3, 4, 5, 6, 7]
print(squareList(numbers))

"""
    Exercise 6: Find Maximum and Minimum
    Find and print the largest and smallest number in a list [8, 2, 15, 1, 9].
"""


def findMaxMin(list):
    print(f'The largest value is {max(list)}\nThe smallest value is {min(list)}')


data = [8, 2, 15, 1, 9]
findMaxMin(data)

"""
    Exercise 7: Count Occurrences
    Count and print how many times 'Football' appears in list. 
"""


def findOccurrences(list, word):
    return list.count(word)


sports = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis']
print(findOccurrences(sports, 'Football'))

"""
    Exercise 8: Sort a list of numbers
    Sort a given list of numbers in ascending order and print it.
"""


def sortList(list):
    print(f'Original list: {list}')
    list.sort()
    print(f'Sorted list: {list}')


numbers = [5, 2, 8, 1, 9]
sortList(numbers)

"""
    Exercise 9: Create a copy of a list
    Create a copy of a list [10, 20, 30] and modify the copy. Print both the original and the copied list to demonstrate they are independent.
"""


def createCopyList(list):
    print(f'Original list: {list}')
    list_2 = list.copy()
    print(f'Copy of a list: {list_2}')


a_certain_list = [10, 20, 30]
createCopyList(a_certain_list)

"""
    Exercise 10: Combine two lists
    Combine given two lists into a single list and print it.
"""


def extendList(list_1, list_2):
    list_1.extend(list_2)
    return list_1


list_a = [1, 2]
list_b = [3, 4]
print(extendList(list_a, list_b))

"""
    Exercise 11: Remove empty strings from the list of strings
"""


def removeEmptyStrings(list):
    new_list = []
    for item in list:
        if item != '':
            new_list.append(item)
        else:
            continue
    return new_list


list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
print(removeEmptyStrings(list1))

"""
    Exercise 12: Remove Duplicates from list
    Write a function that takes a list with duplicate elements and returns a new list with only unique elements. 
"""


def removeDuplicates(list):
    list_no_duplicates = []
    for item in list:
        if item not in list_no_duplicates:
            list_no_duplicates.append(item)
        else:
            continue
    return list_no_duplicates


list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]
print(removeDuplicates(list_with_duplicates))

"""
    Exercise 13: Remove all occurrences of a specific item from a list
    Given a Python list, write a program to remove all occurrences of item 20.
"""


def removeSpecificValue(list, value):
    for item in list:
        if item == value:
            list.remove(value)
    return list


list1 = [5, 20, 15, 20, 25, 50, 20]
print(removeSpecificValue(list1, 20))


"""
    Exercise 14: List Comprehension for Numbers
    Use list comprehension to create a new list containing only the numbers from a given list.
"""

def anotherFunction(list):
    return [item for item in list if isinstance(item, (int, float))]

my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]
print(anotherFunction(my_list))


"""
    Exercise 15: Access Nested Lists
"""

def accessNestedList(list):
    return list[1][1]

nested_list = [[10, 20, 30], [44, 55, 66], [77, 87, 99]]
print(accessNestedList(nested_list))