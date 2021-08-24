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


no_duplicate('Hello')  # False
no_duplicate('World')  # True
no_duplicate('Python')  # True
