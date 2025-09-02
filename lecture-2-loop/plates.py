def isValid(plate):
    if not plate[0:2].isalpha():
        return False

    if not (2 <= len(plate) <= 6):
        return False

    for character in plate:
        count = 0
        if character.isnumeric():
            count += 1
            if count == 1 and character == 0:
                return False

    for character in plate:
        if not character[:len(plate)].isnumeric() and character[:len(plate)].isalpha():
            return False

    if not plate.isalnum():
        return False

    return True


def main():
    plate_number = input('Plate: ')
    if isValid(plate_number):
        print('Valid!')
    else:
        print('Invalid!')


main()
#