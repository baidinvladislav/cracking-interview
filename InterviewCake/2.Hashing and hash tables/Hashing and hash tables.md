# Hashing and hash tables
+ [Inflight Entertainment](#inflight-entertainment)
+ [Permutation Palindrome](#permutation-palindrome)
+ [Word Cloud Data](#word-cloud-data)


## Inflight Entertainment
Дан массив длин фильмов и время полета, определить можно ли полностью занять полет просмотром двух фильмов.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Создаем пустое множество.</li>
 <li>Вычисляем сколько у нас есть свободного времени, если смотрим фильм на этой итерации.</li>
 <li>Если во множестве есть фильм равный по времени свободному времени, то вернуть True.</li>
 <li>Если прошли весь массив с фильмами до конца, то вернуть False.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: [2, 4], 1
Output: False

Example 2:
Input: [2, 4], 6
Output: True

Example 3:
Input: [3, 8], 6
Output: False

Example 4:
Input: [3, 8, 3], 6
Output: True

Example 5:
Input: [1, 2, 3, 4, 5, 6], 7
Output: True

Example 6:
Input: [4, 3, 2], 5
Output: True
```

```python
# their solution
# Time Complexity: O(n),
# Space Complexity: O(n)
def can_two_movies_fill_flight(movie_lengths, flight_length):
    films = set()

    for movie in movie_lengths:
        free_time = flight_length - movie
        if free_time in films:
            return True

        films.add(movie)

    return False

```


## Permutation Palindrome
Определить является ли хотя бы одна перестановка входной строки палиндромом.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Символы смогут образовать палиндром, если только один символ будет нечетного кол-ва, либо все символы будут четным кол-ом.</li>
 <li>Создаем пустое множество.</li>
 <li>Если во множестве нет символа, то добавить символ во множество.</li>
 <li>Если во множестве символ, то удалить символ из множества.</li>
 <li>Если во множестве осталось после всех итераций 1 символ или множество пусто, значит символы могут образовать палиндром, иначе нет .</li>
</ol>

</blockquote></details>


```
Example 1:
Input: 'aabcbcd'
Output: True

Example 2:
Input: 'aabccbdd'
Output: True

Example 3:
Input: 'aabcd'
Output: False

Example 4:
Input: 'aabbcd'
Output: False

Example 5:
Input: ''
Output: True

Example 6:
Input: 'a'
Output: True
```

```python
# their solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def has_palindrome_permutation(the_string):
    s = set()

    for char in the_string:
        if char not in s:
            s.add(char)
        else:
            s.remove(char)

    return len(s) <= 1

```


## Word Cloud Data
