# Write a function that replaces space symbol to '%20'


def replace_spaces(string):
    str_list = list(string)
    final_str = ''

    for i, char in enumerate(str_list):
        if char == ' ':
            str_list.pop(i)
            str_list.insert(i, '%20')

    for i in str_list:
        final_str += i

    return final_str


if __name__ == '__main__':
    test_cases = [
        'John Smith    ',
        'Moscow is a capital ',
        '   cat is not a dog    ',
        '                         ',
        ' hi  my    name    is    Vlad      '
    ]

    for string in test_cases:
        print(replace_spaces(string))
