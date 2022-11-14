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
Дана строка, вернуть кол-во слов в строке.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Определить где в строке начинается и заканчивается слово (много кейсов с пунктуацией).</li>
 <li>Вставлять слова в словарик, ключ==слово, знаечение==кол-во повторений слова в строке.</li>
</ol>

</blockquote></details>


```
Example 1:
Input: 'I like cake'
Output: {'I': 1, 'like': 1, 'cake': 1}

Example 2:
Input: 'aabccbdd'
Output: {'and': 1, 'pound': 1, 'for': 2, 'dessert': 1, 'Chocolate': 1, 'dinner': 1, 'cake': 2}

Example 3:
Input: 'Strawberry short cake? Yum!'
Output: {'cake': 1, 'Strawberry': 1, 'short': 1, 'Yum': 1}

Example 4:
Input: 'Mmm...mmm...decisions...decisions'
Output: {'mmm': 2, 'decisions': 2}

Example 5:
Input: 'Allie's Bakery: Sasha's Cakes'
Output: {"Bakery": 1, "Cakes": 1, "Allie's": 1, "Sasha's": 1}
```

```python
# their solution
# Time Complexity: O(n)
# Space Complexity: O(n)
class WordCloudData:

    def __init__(self, input_string):
        self.words_to_counts = {}
        self.populate_words_to_counts(input_string)

    def populate_words_to_counts(self, input_string):
        # Iterates over each character in the input string, splitting
        # words and passing them to add_word_to_dictionary()
        current_word_start_index = 0
        current_word_length = 0
        for i, character in enumerate(input_string):

            # If we reached the end of the string we check if the last
            # character is a letter and add the last word to our dictionary
            if i == len(input_string) - 1:
                if character.isalpha():
                    current_word_length += 1
                if current_word_length > 0:
                    current_word = input_string[
                        current_word_start_index:current_word_start_index + current_word_length
                    ]

                    self.add_word_to_dictionary(current_word)

            # If we reach a space or emdash we know we're at the end of a word
            # so we add it to our dictionary and reset our current word
            # '\u2014 == '—'
            elif character == ' ' or character == '\u2014':
                if current_word_length > 0:
                    current_word = input_string[
                        current_word_start_index:current_word_start_index + current_word_length
                    ]

                    self.add_word_to_dictionary(current_word)
                    current_word_length = 0

            # We want to make sure we split on ellipses so if we get two periods in
            # a row we add the current word to our dictionary and reset our current word
            elif character == '.':
                if i < len(input_string) - 1 and input_string[i + 1] == '.':
                    if current_word_length > 0:
                        current_word = input_string[
                            current_word_start_index:current_word_start_index + current_word_length
                        ]

                        self.add_word_to_dictionary(current_word)
                        current_word_length = 0

            # If the character is a letter or an apostrophe, we add it to our current word
            elif character.isalpha() or character == '\'':
                if current_word_length == 0:
                    current_word_start_index = i
                current_word_length += 1

            # If the character is a hyphen, we want to check if it's surrounded by letters
            # If it is, we add it to our current word
            elif character == '-':
                if i > 0 and input_string[i - 1].isalpha() and input_string[i + 1].isalpha():
                    current_word_length += 1
                else:
                    if current_word_length > 0:
                        current_word = input_string[
                            current_word_start_index:current_word_start_index + current_word_length
                        ]

                        self.add_word_to_dictionary(current_word)
                        current_word_length = 0

    def add_word_to_dictionary(self, word):
        # If the word is already in the dictionary we increment its count
        if word in self.words_to_counts:
            self.words_to_counts[word] += 1

        # If a lowercase version is in the dictionary, we know our input word must be uppercase
        # but we only include uppercase words if they're always uppercase
        # so we just increment the lowercase version's count
        elif word.lower() in self.words_to_counts:
            self.words_to_counts[word.lower()] += 1

        # If an uppercase version is in the dictionary, we know our input word must be lowercase.
        # since we only include uppercase words if they're always uppercase, we add the
        # lowercase version and give it the uppercase version's count
        elif word.capitalize() in self.words_to_counts:
            self.words_to_counts[word] = 1
            self.words_to_counts[word] += self.words_to_counts[word.capitalize()]
            del self.words_to_counts[word.capitalize()]

        # Otherwise, the word is not in the dictionary at all, lowercase or uppercase
        # so we add it to the dictionary
        else:
            self.words_to_counts[word] = 1

```
