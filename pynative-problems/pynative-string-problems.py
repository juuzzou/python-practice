from math import floor
from string import ascii_lowercase, ascii_uppercase, ascii_letters, digits
"""
    Exercise 1A: Create a string made of the first, middle and last character
    Write a program to create a new string made of an input string’s first, middle, and last character.
"""
def createNewString(string):
    new_string = string[0] + string[round(len(string)/2)] + string[len(string) - 1]
    return print(new_string)

"""
    Exercise 1B: Create a string made of the middle three characters
    Write a program to create a new string made of the middle three characters of an input string.
"""

def createNewStringMiddleChars(string):
    new_string = string[floor(len(string)/2) - 1] + string[floor(len(string)/2)] + string[floor(len(string)/2) + 1]
    return print(new_string)

def start():
    problem = input("Choose the problem (A, B): ")
    if problem == 'A':
        user_input = str(input("Enter your string: "))
        createNewString(user_input)
    else:
        user_input = str(input("Enter your string: "))
        createNewStringMiddleChars(user_input)

"""
    Exercise 2: Append new string in the middle of a given string
    Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
"""

def insertString(string_a, string_b):
    new_string = string_a[0:floor(len(string_a)/2)] + string_b + string_a[floor(len(string_a)/2):floor(len(string_a))]
    return print(new_string)

insertString("Ault", "Kelly")

"""
    Exercise 3: Create a new string made of the first, middle, and last characters of each input string
    Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.
"""

def buildString(string_a, string_b):
    new_string = string_a[0] + string_b[0] + string_a[floor(len(string_a) / 2)] + string_b[floor(len(string_b) / 2)] + \
                 string_a[len(string_a) - 1] + string_b[len(string_b) - 1]
    return print(new_string)

buildString("America", "Japan")

"""
    Exercise 4: Arrange string characters such that lowercase letters should come first
    Given string contains a combination of the lower and upper case letters. 
    Write a program to arrange the characters of a string so that all lowercase letters should come first.
"""

def arrangeString(input_string):
    new_string = ''
    for character in input_string:
        if character in ascii_lowercase:
            new_string += character
        else:
            continue
    for character in input_string:
        if character in ascii_uppercase:
            new_string += character
        else:
            continue
    return print(new_string)

arrangeString("PyNaTive")

"""
    Exercise 5: Count all letters, digits, and special symbols from a given string
"""

def countDiffChars(input_string):
    chars_count = 0
    digit_count = 0
    symbol_count = 0
    for char in input_string:
        if char in ascii_letters:
            chars_count += 1
        elif char in digits:
            digit_count += 1
        else:
            symbol_count += 1

    return print(f'Total count of chars - {chars_count}, digits - {digit_count}, symbols - {symbol_count}')

countDiffChars("P@#yn26at^&i5ve")

"""
    Exercise 6: Create a mixed String using the following rules
    Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, 
    Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
"""

def createMixString(string_a, string_b):
    new_string = ""
    string_b = string_b[::-1]
    for i in range(max(len(string_a), len(string_b))):
        new_string += string_a[i]
        new_string += string_b[i]
    return print(new_string)

createMixString("Abc", "Xyz")