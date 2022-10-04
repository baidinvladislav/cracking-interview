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


## Word Cloud Data
