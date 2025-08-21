"""
    Exercise 1: Perform Basic Set Operations
        Create a Set: Create a set named fruits containing “apple”, “banana”, “mango”, and “orange”.
        Add Element: Add “grape” to the fruits set.
        Remove Element: Remove “banana” from the fruits set.
        Discard Element: Try to discard “mango” from the fruits set.
"""


def setOperations(*args):
    new_set = set()
    for item in args:
        new_set.add(item)

    new_set.add("grape")
    new_set.remove("banana")
    new_set.discard("mango")
    return new_set


print(setOperations("apple", "orange", "mango", "banana"))

"""
    Exercise 2: Union of Sets
    Find the union of set1 and set2. Write a Python program to return a new set with unique items from both sets by removing duplicates.
"""


def unionSet(set_1, set_2):
    return set_1 | set_2


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(unionSet(set1, set2))

"""
    Exercise 3: Intersection of Sets
    Find the intersection of set1 and set2. Write a code to return a new set containing only the elements that are common to both set1 and set2
"""


def intersectionSet(set_1, set_2):
    return set_1 & set_2


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(intersectionSet(set1, set2))
