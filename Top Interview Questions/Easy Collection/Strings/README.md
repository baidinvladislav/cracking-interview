# Array
+ [Reverse String](#reverse-string)
+ [Valid Anagram](#valid-anagram)


## Reverse String
Развернуть строку.

https://leetcode.com/problems/reverse-string/

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Используем два указателя.</li>
 <li>На каждой итерации свапаем элементы пока указатели не встретятся где то в середине.</li>
 <li>На каждой итерации инкрементируем левый указатель и декрементируем правый указатель.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: ["h", "e", "l", "l", "o"]
Output: ["o", "l", "l", "e", "h"]

Example 2:
Input: ["h", "a", "n", "n", "a", "H"]
Output: ["H", "a", "n", "n", "a", "h"]

Example 3:
Input: ["a", "s", "d"]
Output: ["d", "s", "a"]
```

```python
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

```


## Valid Anagram
Даны две строки, определить, что они диаграммы.

https://leetcode.com/problems/valid-anagram/

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Перевести строки в массив.</li>
 <li>Если размер строк отличается, то сразу False.</li>
 <li>Остортировать.</li>
 <li>Сравнить.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: s = "anagram", t = "nagaram"
Output: True

Example 2:
Input: s = "rat", t = "car"
Output: False
```

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s, t = list(s), list(t)

        s.sort()
        t.sort()

        return s == t

```
