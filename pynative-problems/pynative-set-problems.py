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

"""
    Exercise 4: Difference of Sets
    Find the difference (set1 - set2). Write a code to returns a new set containing elements that are present in set1 but not in set2.
"""


def differenceSet(set_1, set_2):
    return set_1 - set_2


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(differenceSet(set1, set2))

"""
    Exercise 5: Symmetric Difference
    Find the symmetric difference of set1 and set2. 
    Write a code to returns a new set containing elements that are unique to either set1 or set2, but not in both. 
    It’s like finding the union and then removing the intersection.
"""


def symmetricDifferenceSet(set_1, set_2):
    return set_1 ^ set_2


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(symmetricDifferenceSet(set1, set2))

"""
    Exercise 6: Add a list of Elements to a Set
    Given a Python list, write a program to add all of its elements into a given set.
"""


def addListToSet(a_list, a_set):
    for item in a_list:
        a_set.add(item)
    return a_set


sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
print(addListToSet(sample_list, sample_set))

"""
    Exercise 7: Set Difference Update
    Given two Python sets, write a program to update the first set with only the items that are unique to it (i.e., not present in the second set).
"""


def updateDifferenceSet(set_1, set_2):
    set_1.difference_update(set_2)
    return set_1


set1 = {10, 20, 30}
set2 = {20, 40, 50}
print(updateDifferenceSet(set1, set2))

"""
    Exercise 8: Remove Items From Set Simultaneously
    Write a Python program to remove items 10, 20, 30 from the following set at once.
"""


def removeItem(set):
    remove_set = {10, 20, 30}
    set.difference_update(remove_set)
    return set


set1 = {10, 20, 30, 40, 50}
print(removeItem(set1))

"""
    Exercise 9: Check Subset
    Check if set1 is a subset of set2. Write a code to return True if every element in the subset_set is also present in the main_set.
"""


def isSubset(set_1, set_2):
    return set_1.issubset(set_2)


subset_set = {10, 20}
main_set = {10, 20, 30, 40}
print(isSubset(subset_set, main_set))

"""
    Exercise 10: Check Superset
    Check if main_set = {10, 20, 30, 40} is a superset of subset_set = {10, 20}.
"""


def isSuperset(set_1, set_2):
    return set_1.issuperset(set_2)


set1 = {10, 20}
set2 = {10, 20, 30, 40}
print(isSubset(set1, set2))

