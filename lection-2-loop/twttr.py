def removeVowels(string):
    for char in string:
        if char in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
            string = string.replace(char, '')
        else:
            continue
    return print(string)

removeVowels('Twitter')
removeVowels("What's your name?")
removeVowels('CS50')

#