# Write a function which determines that string is permutation of palindrome


def check_palindrome(string):
    storage = {}
    for char in string:
        if char in storage:
            storage[char] += 1
        else:
            storage[char] = 1

    odd_char = []
    for key, value in storage.items():
        if key != ' ' and value % 2 != 0:
            odd_char.append(key)

    if len(odd_char) > 1:
        print(f'String -{string}- is not palindrome')
        return False
    else:
        print(f'String -{string}- is palindrome')
        return True


if __name__ == '__main__':
    test_cases = [
        # True cases
        'ашашл',  # шалаш
        'динез ванаразен ан ивд',  # диван незаразен на вид
        'реувен иер ен ву',  # уверен и не реву

        # False cases
        'эттом леал я читого мнпро имкниг',  # этим летом я прочитал много книг
        'эжныйто неслоалго ритм',  # это несложный алгоритм
        'г элето жит иде в каккодир ойовке'  # где это лежит и в какой кодировке
    ]

    for string in test_cases:
        print(check_palindrome(string))
