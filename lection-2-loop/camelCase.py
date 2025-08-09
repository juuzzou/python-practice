def toSnakeCase(string):
    snake_case = ''
    for char in string:
        if char.isupper():
            snake_case = snake_case + '_' + char.lower()
        else:
            snake_case += char
    return snake_case


def main():
    print(toSnakeCase('camelCase'))

main()
#

