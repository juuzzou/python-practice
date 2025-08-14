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

"""
    Exercise 3: Slice list into 3 equal chunks and reverse each chunk
"""


def sliceList(list):
    list_1, list_2, list_3 = [], [], []
    _temp = len(list)
    for item_1, item_2, item_3 in zip(range(0, _temp // 3), range(_temp // 3, 2 * _temp // 3),
                                      range(2 * _temp // 3, _temp)):
        list_1.append(list[item_1])
        list_2.append(list[item_2])
        list_3.append(list[item_3])
    print(f'List 1: {list_1[::-1]}\nList 2: {list_2[::-1]}\nList 3: {list_3[::-1]}')


sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
sliceList(sample_list)
