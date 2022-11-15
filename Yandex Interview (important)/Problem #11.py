"""
Написать функцию, которая принимает строку.
Для заданной строки функция вернёт словарь, где для каждого символа
указано максимальное количество непрерывных повторений
этого символа в строке.
Например, для строки "aafbaaaaffc" результат будет:
{
    'a': 4,
    'b': 1,
    'f': 2,
    'c': 1,
}

"aafbaaaaffc"

start = 0
end = 0

1. d = {}
2. for end in range(1, len(str))
3. if string[end] != string[i - 1] который будет сжимать => start = end
4. d[char] = max(d[char], window_count)
5. return d
"""


def f(string):
    window_count, d = 1, {}

    for i in range(1, len(string)):
        if string[i - 1] == string[i]:
            window_count += 1
        else:
            d[string[i - 1]] = max(d.get(string[i - 1], 0), window_count)
            window_count = 1

    d[string[i - 1]] = max(d[string[i - 1]], window_count)
    return d
