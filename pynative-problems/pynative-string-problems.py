"""
    Exercise 1A: Create a string made of the first, middle and last character
    Write a program to create a new string made of an input string’s first, middle, and last character.
"""
def createNewString(string):
    new_string = string[0] + string[round(len(string)/2)] + string[len(string) - 1]
    return print(new_string)

def main():
    user_input = str(input("Enter your string: "))
    createNewString(user_input)

main()