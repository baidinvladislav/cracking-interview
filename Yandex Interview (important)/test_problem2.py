"""
Дана строка (возможно, пустая), состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
И сгенерирует ошибку, если на вход пришла невалидная строка.

Пояснения: Если символ встречается 1 раз, он остается без изменений;
Если символ повторяется более 1 раза, к нему добавляется количество повторений.
"""


def solution(string):
    if len(string) < 2:
        return str(string[0])

    result, counter = "", 1
    for i in range(1, len(string)):
        if string[i - 1] == string[i]:
            counter += 1
        else:
            result += f"{string[i - 1]}{counter if counter != 1 else ''}"
            counter = 1

    result += f"{string[i]}{counter if counter != 1 else ''}"
    return result


def test_first():
    string = "AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB"
    expect = "A4B3C2XYZD4E3F3A6B28"

    assert expect == solution(string)


def test_second():
    string = "TTTPPPJJKRR"
    expect = "T3P3J2KR2"

    assert expect == solution(string)


def test_third():
    string = "AAABBC"
    expect = "A3B2C"

    assert expect == solution(string)


def test_fourth():
    string = "GGGGGGGGGGGGFFA"
    expect = "G12F2A"

    assert expect == solution(string)


def test_fifth():
    string = "A"
    expect = "A"

    assert expect == solution(string)


def test_seventh():
    string = "AAABBCCF"
    expect = "A3B2C2F"

    assert expect == solution(string)


def test_eighth():
    string = "AAABBCF"
    expect = "A3B2CF"

    assert expect == solution(string)


def test_ninth():
    string = "ABC"
    expect = "ABC"

    assert expect == solution(string)
