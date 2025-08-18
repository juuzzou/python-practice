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

"""
    Exercise 3: Dictionary from Lists
    Write a Python program to convert two Python lists into a dictionary where elements from the first list become keys 
    and elements from the second list become values.
"""


def toDict(keys, values):
    dictionary = {}
    for key, value in zip(keys, values):
        dictionary.update({key: value})
    return dictionary


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
print(toDict(keys, values))

"""
    Exercise 4: Clear Dictionary
    Clear all key-value pairs from a given dictionary and print it.
"""


def clearDict(dictionary):
    dictionary.clear()
    return dictionary


my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
print(clearDict(my_dict))

"""
    Exercise 5: Merge two Python dictionaries into one 
    Write a code to merge two dictionaries into a new dictionary and print it.   
"""


def mergeDicts(first_dictionary, second_dictionary):
    first_dictionary.update(second_dictionary)
    return first_dictionary


dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
print(mergeDicts(dict1, dict2))

"""
    Exercise 6: Count Character Frequencies
    Given a string, create a dictionary where keys are characters and values are their frequencies in the string.
"""


def countAllChars(string):
    counter = {}
    for character in string:
        count = string.count(character)
        counter[character] = count
    return print(counter)


string1 = 'Jessa'
countAllChars(string1)

"""
    Exercise 7: Access Nested Dictionary
    Given a nested dictionary {'person': {'name': 'Alice', 'age': 30}}, print Alice’s age.
"""


def accessNestedDict(dictionary):
    return dictionary['person']['age']


data = {'person': {'name': 'Alice', 'age': 30}}
print(f'Age: {accessNestedDict(data)}')

"""
    Exercise 8: Print the value of key ‘history’ from nested dict
"""


def notANamedFunc():
    _sampleDict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }
    return _sampleDict['class']['student']['marks']['history']


print(notANamedFunc())

"""
    Exercise 9: Modify Nested Dictionary
    In the below dictionary, change name to ‘Jessa’.
"""


def notANamedFunc_2(name):
    _sampleDict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }
    _sampleDict['class']['student'].update({'name': name})
    return _sampleDict


print(notANamedFunc_2("Jessa"))
