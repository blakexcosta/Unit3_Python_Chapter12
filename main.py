def main():
    print("hello")
    # hashmaps = dictionarie sin python

    # Python dictionary
    phone_book = {
        'Mom': 29,
        'Dad': 30
    }
    print(phone_book['Mom'])
    # can store different types in dictionary
    phone_book = {
        'Mom': "8458072456",
        'SSN': 123456789
    }
    print(phone_book['SSN'])

    # Change existing dictionary value
    phone_book['SSN'] = 456789123
    print(phone_book['SSN'])

    # Add new dictionary key/value pair
    phone_book['Phone_Number'] = "845123456"
    print(phone_book['Phone_Number'])

    # Remove key value pair
    del phone_book['Phone_Number']
    print(phone_book)

    # Dictionary Methods:
    # https://education.launchcode.org/lchs/chapters/dictionaries/dictionary-methods.html

    # Loop through keys
    for key in phone_book.keys():
        print(key)

    # Loop through values
    for value in phone_book.values():
        print(value)

    # print the keys and values
    for key, value in phone_book.items():
        print(f"{key}: {value}")

    # search a dictionary
    print("Mom" in phone_book)
    print("bobb" not in phone_book)


if __name__ == "__main__":
    main()
