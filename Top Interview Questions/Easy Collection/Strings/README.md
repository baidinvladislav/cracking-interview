# Array
+ [Reverse String](#reverse-string)
+ [Valid Anagram](#valid-anagram)
+ [Reverse Integer](#reverse-integer)
+ [First Unique Character in a String](#first-unique-character-in-a-string)


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


## Valid Palindrome
Определить, что строка является палиндромом.

https://leetcode.com/problems/valid-palindrome/

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Два указателя, один на начале стоки, второй на конце.</li>
 <li>Идем указателями навстречу друг другу пока они не втретятся, попутно проскаем не валидные символы (пробелы и знаки пунктуации).</li>
 <li>Если символы под указателяими не равны, то вернуть False, если прошли весь цикл до конца и указатели встретились, вернуть True.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

```python
class Solution:
    
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

```


## Reverse Integer
Развернуть число.

https://leetcode.com/problems/reverse-integer/

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Привести к строке модуль числа из инпута.</li>
 <li>Развернуть число как обычную строку срезом.</li>
 <li>Привести к числу развернутую строку, если на инпуте было отрицательное число, то вернуть результат в отрицательной форме, иначе вернуть просто результат.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21
```

```python
class Solution:
    def reverse(self, x: int) -> int:
        to_str = str(abs(x))
        reversed_str = to_str[::-1]
        result = int(reversed_str)
        return -result if x < 0 else result

```



## First Unique Character in a String
Найти первый уникальный элемент в строке.

https://leetcode.com/problems/first-unique-character-in-a-string/

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Подсчитать количество всех элементов в мапе.</li>
 <li>Идти по строке, обращаясь к ключам мапы, вернуть индекса первожего элемента в мапе которого значением является 1.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: "leetcode"
Output: 0

Example 2:
Input: "loveleetcode"
Output: 2

Example 3:
Input: "aabb"
Output: -1
```

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1

        for i in range(len(s)):
            if d[s[i]] == 1:
                return i

        return -1

```
