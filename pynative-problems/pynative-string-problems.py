from math import floor
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

def main():
    problem = input("Choose the problem (A, B): ")
    if problem == 'A':
        user_input = str(input("Enter your string: "))
        createNewString(user_input)
    else:
        user_input = str(input("Enter your string: "))
        createNewStringMiddleChars(user_input)

main()