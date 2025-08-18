"""
    Exercise 1: Perform basic dictionary operations
    Perform following operations on given dictionary:
    Add New Key-Value Pair: Add a new key-value pair, 'profession': 'Doctor', to the dictionary and print the updated dictionary.
    Modify Value: Change the value of the age key to 40 in the dictionary and print the updated dictionary.
    Access Key: Print the value associated with the city key.
"""


def dictionaryOperations(dictionary):
    dictionary.update({'profession': 'Doctor'})
    dictionary.update({'age': 40})
    print(dictionary)
    print(dictionary.get('city'))


my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
dictionaryOperations(my_dict)
