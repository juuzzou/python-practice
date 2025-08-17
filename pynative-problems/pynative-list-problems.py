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
