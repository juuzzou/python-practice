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