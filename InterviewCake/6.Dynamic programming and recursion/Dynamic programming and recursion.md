# Dynamic programming and recursion
+ [Recursive String Permutations](#recursive-string-permutations)
+ [Compute the nth Fibonacci Number](#compute-the-nth-fibonacci-number)
+ [Making Change](#making-change)
+ [Cake Thief](#cake-thief)


## Recursive String Permutations
Дана строка, нужно вернуть все возможные перестановки строки.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>БС: длина строки == 1.</li>
 <li>Рекурсивно собрать все подстроки и добавлять в подстроки первый элемент в начало строки.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: 'AB'
Output: ['AB', 'BA']

Example 2:
Input: 'ABC'
Output: ['ABC', 'BAC', 'BCA', 'ACB', 'CAB', 'CBA']

Example 3:
Input: 'ABCD'
Output: ['ABCD', 'BACD', 'BCAD', 'BCDA', 'ACBD', 'CABD', 'CBAD', 'CBDA', 'ACDB', 'CADB', 'CDAB', 'CDBA', 'ABDC', 'BADC', 'BDAC', 'BDCA', 'ADBC', 'DABC', 'DBAC', 'DBCA', 'ADCB', 'DACB', 'DCAB', 'DCBA']

```

```python
# cracking the coding interview solution
def generate_permutations(text):
    if len(text) == 1:
        return [text]

    results = []
    first = text[0]
    remainder = text[1:]

    words = generate_permutations(remainder)
    for word in words:
        for i in range(len(word) + 1):
            # insert first char at each index/position of word
            s = word[:i] + first + word[i:]
            results.append(s)

    return results

```


## Compute the nth Fibonacci Number


## Making Change


## Cake Thief
