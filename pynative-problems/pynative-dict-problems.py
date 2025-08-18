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

"""
    Exercise 2: Perform dictionary operations
    Perform following operations on given dictionary
        Remove Key-Value Pair : Remove the profession key-value pair from the dictionary.
        Get Items (Key-Value Pairs): Print all key-value pairs (items) in the dictionary.
        Check if Key Exists in the dictionary

"""


def anotherDictionaryFunction(dictionary):
    dictionary.pop('profession')
    for key, value in dictionary.items():
        print(f'{key}: {value}')


def ifExists(dictionary, key):
    return key in dictionary


my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
anotherDictionaryFunction(my_dict)
print(ifExists(my_dict, key='age'))
