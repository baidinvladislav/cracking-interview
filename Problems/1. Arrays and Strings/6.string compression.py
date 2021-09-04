"""
Write a function which compressions strings
"""


def to_compress(string):
    storage = {}
    for char in string:
        if char in storage:
            storage[char] += 1
        else:
            storage[char] = 1

    final_str = ''
    for key, value in storage.items():
        container = key + str(value)
        final_str += container

    return final_str


if __name__ == '__main__':
    test_cases = [
        'aawwweeerrrtt',
        'xxxzzzasdgvfff',
        'qwerttyu',
        'poiybsasaasdscznxg'
    ]

    for string in test_cases:
        print(to_compress(string))
