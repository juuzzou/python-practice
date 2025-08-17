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
