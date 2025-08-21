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
