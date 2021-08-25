def no_duplicate(string):
    storage = {}
    for character in string:
        if character in storage:
            print(f'String -{string}- contains duplicates of -{character}- character')
            return False
        else:
            storage[character] = 1
    print(f'String -{string}- does not contain any character duplicates')
    return True


if __name__ == '__main__':
    test_cases = [
        'Hello',
        'World',
        'Python',
        'qweasd',
        'zxcvbnz'
    ]

    for string in test_cases:
        no_duplicate(string)
        print(string)
