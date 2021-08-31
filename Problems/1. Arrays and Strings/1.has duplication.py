# Write a function to determine that string has duplicates character


def no_duplicate(string):
    storage = {}
    for character in string:
        if character in storage:
            return f'String -{string}- contains duplicates of -{character}- character', True
        else:
            storage[character] = 1
    return f'String -{string}- does not contain any character duplicates', False


if __name__ == '__main__':
    test_cases = [
        'Hello',
        'World',
        'Python',
        'qweasd',
        'zxcvbnz'
    ]

    for string in test_cases:
        print(no_duplicate(string))
