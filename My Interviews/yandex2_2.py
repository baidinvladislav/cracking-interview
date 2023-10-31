"""
Даны две строки s и t. Определите изоморфны ли они.

Определение:
Две строки s и t называются изоморфными, если можно сделать замену символов в строке s,
чтобы получить строку t, при этом:
1. Все вхождения заменяемого символа должны быть заменены заменяющим символом
2. Никакие два разных символа не могут быть заменены на один и тот же символ
3. Символ может быть заменен сам на себя


Примеры:
s = "egg", t = "add" -> True
s = "foo", t = "bar" -> False
s = "paper", t = "title" -> True
"""


# s = "egg", t = "add"
# d1 = {e: a, g: d}
# d2 = {a: e, d: g}

# d1, d2 = {e: a, g: d}, {a: e, d: g}

# d1, d2 = {}, {}


# s = "foo", t = "bar"
# d1 = {f: b, o: r}
# d2 = {b: f, a: o, r: o}


# time: O(N)
# space: O(N^2)
def solution(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    d1, d2 = {}, {}

    for i in range(len(s)):
        d1[s[i]] = t[i]

    for i in range(len(t)):
        d2[t[i]] = s[i]

    if len(d1) != len(d2):
        return False

    for char in s:
        val = d1[char]
        if d2[val] != char:
            return False

    return True

    # ====


"""
Дана строка и натуральное число k.
Требуется найти длину максимальной подстроки, содержащей не более k различных символов.
"acaba", k = 2 -> 3 ("aca")
"aaa", k = 1 -> 3 ("aaa")
"""


# s = acaba
# start = 2
# end = 2
# k = 2
# result = 3
# d = {a: 2, b: 1}
# time: O(N)
# space: O(N)
def solution(s: str, k: int) -> int:
    start = 0
    result = 0
    d = defaultdict(int)

    for end in range(len(s)):
        d[s[end]] += 1

        while len(d) > k:
            d[s[start]] -= 1
            if d[s[start]] == 0:
                del d[s[start]]

            start += 1

        result = max(result, end - start + 1)

    return result
