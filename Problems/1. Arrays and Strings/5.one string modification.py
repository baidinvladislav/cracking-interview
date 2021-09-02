# Write a function that determines that two strings can be converted in one step


def check_one_step(string1, string2):
    str_list = list(string1)

    for i in string2:
        try:
            str_list.remove(i)
        except ValueError:
            continue

    if len(str_list) > 1:
        return False
    else:
        return True


if __name__ == '__main__':
    test_cases = [
        ('pale', 'ple'),
        ('pales', 'pale'),
        ('pale', 'bale'),
        ('pale', 'bake')
    ]

    for case in test_cases:
        print(check_one_step(case[0], case[1]))
