from math import floor
from string import ascii_lowercase, ascii_uppercase, ascii_letters, digits, punctuation

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

"""
    Exercise 7: String characters balance Test
    Write a program to check if two strings are balanced. 
    For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. 
    The character’s position doesn’t matter.
"""

def isInString(string_a, string_b):
    if string_a in string_b:
        return True
    else:
        return False

test_result_1 = isInString("Yn","PYnative")
test_result_2 = isInString("Ynf","PYnative")
print(test_result_1, test_result_2)

"""
    Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
    Write a program to find all occurrences of “USA” in a given string ignoring the case. 
"""

def countSubstringOccurrences(string, substring):
    return print(string.upper().count(substring.upper()))

text = "Welcome to USA. usa awesome, isn't it?"
countSubstringOccurrences(text, 'usa')

"""
    Exercise 9: Calculate the sum and average of the digits present in a string
    Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters. 
"""

def calculateSumAndAvgInString(string):
    _temp_list = []
    for character in string:
        if character in digits:
            _temp_list.append(int(character))
        else:
            continue
    return print(f'SUM: {sum(_temp_list)}, AVG: {sum(_temp_list)/len(_temp_list):.2f} ')

calculateSumAndAvgInString("PYnative29@#8496")

"""
    Exercise 10: Write a program to count occurrences of all characters within a string
"""

def countAllChars(string):
    counter ={}
    for character in string:
        count = string.count(character)
        counter[character] = count
    return print(counter)

countAllChars("Apple")

"""
    Exercise 11: Reverse a given string
"""

def reverserString(string):
    return print(string[::-1])

reverserString("PYnative")

"""
    Exercise 12: Find the last position of a given substring
    Write a program to find the last position of a substring “Emma” in a given string.
"""
def findLastPosition(string, substring):
    return print(f'Last occurrence of Emma starts at index {string.rfind(substring)}')

test_text = "Emma is a data scientist who knows Python. Emma works at google."
findLastPosition(test_text, 'Emma')

"""
    Exercise 13: Split a string on hyphens
    Write a program to split a given string on hyphens and display each substring.
"""

def splitBy(string):
    string = string.split(sep='-')
    for word in string:
        print(word)
splitBy("Emma-is-a-data-scientist")

"""
    Exercise 14: Remove empty strings from a list of strings
"""
def removeEmptyString(list):
    for element in list:
        if element is None or element == "":
            list.remove(element)
        else:
            continue
    return print(list)

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
removeEmptyString(str_list)

"""
    Exercise 15: Remove special symbols / punctuation from a string
"""

""""
    Shit code
"""

def removeSymbols(string):
    new_string = ''
    for letter in string:
        if letter in punctuation:
            continue
        else:
            new_string += letter

    new_string = new_string.split(' ')

    for word in new_string:
        if word == '':
            new_string.remove(word)
        else:
            continue

    temp = ' '.join(map(str, new_string))
    return temp

print(removeSymbols("/*Jon is @developer & musician"))

"""
    Exercise 16: Removal all characters from a string except integers
"""
def removeExceptInt(string):
    result = ""
    for item in string:
        if item.isdigit():
            result += item
    return result

print(removeExceptInt('I am 25 years and 10 months old'))

"""
    Exercise 17: Find words with both alphabets and numbers
    Write a program to find words with both alphabets and numbers from an input string.
"""

def printWhereAlphaNum(string):
    list_ = string.split(" ")
    yet_another_list = []
    for item in list_:
        if any(char in ascii_letters for char in item) and any(char in digits for char in item):
            yet_another_list.append(item)
        else:
            continue
    return yet_another_list

str1 = "Emma25 is Data scientist50 and AI Expert"
print(printWhereAlphaNum(str1))

"""
    Exercise 18: Replace each special symbol with # in the following string
"""
def replaceSymbolWithHash(string):
    for char in string:
        if char in punctuation:
            string = string.replace(char, "#")
        else:
            continue
    return string
str1 = '/*Jon is @developer & musician!!'
print(replaceSymbolWithHash(str1))