"""
    Exercise 1: List Creation using two lists
    Write a code to create a new list using odd-indexed elements from the first list and even-indexed elements from the second
    Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.
"""
def createListOfTwo(list_1, list_2):
    _temp = []
    print(f'Odd: {list_1[1::2]}')
    print(f'Odd: {list_2[::2]}')
    _temp.extend(list_1[1::2])
    _temp.extend(list_2[::2])
    return _temp

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

print(createListOfTwo(l1, l2))

"""
    Exercise 2: Remove and add item in a list
    Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
"""

def anotherFunction(list, new_element):
    list.pop(4)
    list.insert(2, new_element)
    list.append(new_element)
    return list
list1 = [54, 44, 27, 79, 91, 41]
print(f'List before manipulations: {list1}')
print(f'List after manipulations: {anotherFunction(list1, 5)}')
