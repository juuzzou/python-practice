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

"""
    Exercise 4: Count the occurrence of each element from a list
    Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element.
"""


def countItems(list):
    count_dict = {}
    for item in list:
        counter = list.count(item)
        count_dict.update({item: counter})
    return count_dict


sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
test = countItems(sample_list)
print(test)

"""
    Exercise 5: Paired Elements from Two Lists as a Set
    Write a code to create a Python set such that it shows the element from both lists in a pair.
"""


def pairElement(list_1, list_2):
    result = zip(list_1, list_2)
    return set(result)


first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]
print(pairElement(first_list, second_list))

"""
    Exercise 6: Set Intersection and Removal
    Write a code to find the intersection (common) of two sets and remove those elements from the first set.
"""


def yetAnotherFunction(set_1, set_2):
    intersect = set_1.intersection(set_2)
    for item in intersect:
        set_1.remove(item)
    print(f'Intersection is {intersect}\nFirst Set after removing common element: {set_1}')


first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

yetAnotherFunction(first_set, second_set)

"""
    Exercise 7: Subset or Superset of another set
    Write a code to checks if one set is a subset or superset of another set. If found, delete all elements from that set.
"""


def andAnotherFunction(set_1, set_2):
    print(f'First set is subset of second set - {set_1.issubset(set_2)}')
    print(f'Second set is subset of First set - {set_2.issubset(set_1)}')
    print(f'First set is Super set of second set - {set_1.issuperset(set_2)}')
    print(f'Second set is Super set of First set - {set_2.issuperset(set_1)}')

    if set_1.issubset(set_2):
        set_1.clear()

    if set_2.issubset(set_1):
        set_2.clear()

    print(set_1, set_2)


first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}
andAnotherFunction(first_set, second_set)
