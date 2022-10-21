"""
Дана строка (возможно, пустая), состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
И сгенерирует ошибку, если на вход пришла невалидная строка.
Пояснения: Если символ встречается 1 раз, он остается без изменений;
Если символ повторяется более 1 раза, к нему добавляется количество повторений.\
"""


def f(string):
    string += '#'
    counter = 0
    result = ''
    for i in range(1, len(string)):
        if string[i - 1] == string[i]:
            counter += 1
        else:
            if counter == 0:
                result += string[i - 1]
            else:
                result += f'{counter + 1}{string[i - 1]}'
                counter = 0

    return result


print(f('AAABBCCF') == '3A2B2CF')
print(f('AAABBCF') == '3A2BCF')
print(f('ABC') == 'ABC')


class Solution:
    def f(self, s):
        if not s:
            return 'на вход пришла невалидная строка'

        s += '#'
        result = ''
        p1, p2 = 0, 1

        while p2 != len(s):
            if s[p1] == s[p2]:
                p2 += 1
            else:
                result += f'{p2 - p1}{s[p1]}' if p2 - p1 != 1 else f'{s[p1]}'
                p1 = p2
        return result


print(Solution().f(s='AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'))
print(Solution().f(s=''))
