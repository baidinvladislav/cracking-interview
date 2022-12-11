# Combinatorics, probability, and other math
+ [Which Appears Twice](#which-appears-twice)
+ [Find in Ordered Set](#find-in-ordered-set)
+ [Inplace Shuffle](#inplace-shuffle)
+ [Simulate 5-sided die](#simulate-5-sided-die)
+ [Simulate 7-sided die](#simulate-7-sided-die)
+ [Two Egg Problem](#two-egg-problem)


## Which Appears Twice
Дан массив чисел в диапазоне от 1 до n, одно из чисел присутствует в массиве дважды, вернуть это число.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Зная, длину массива мы можем быстро вычислить корректную сумму массива через формулу.</li>
 <li>Посчитаем актуальную сумму для входного массива.</li>
 <li>Разница между корректной и актуальной суммой будет являться искомым числом.</li>
</ol>

</blockquote></details>


```python
# my code
# Time Complexity: O(n)
# Space Complexity: O(1)
def find_repeat(numbers_list):
    if len(numbers_list) < 2:
        raise ValueError('Finding duplicate requires at least two numbers')

    n = len(numbers_list) - 1
    correct_sum = (n * n + n) / 2
    actual_sum = sum(numbers_list)
    return actual_sum - correct_sum

```


## Find in Ordered Set
Дан отсортирвоанный массив чисел и число, определить есть ли число в массиве.

<details><summary>Решение через Бинарный поиск:</summary><blockquote>

<ol>
 <li>На каждой итерации вычисляем индекс по середине массиве.</li>
 <li>Если текущее значение под средним индексом больше нашего значения, то смотрим левой части массива.</li>
 <li>Если текущее значение под средниим индексом меньше искомого значения, то смотрим в правой части массива.</li>
</ol>

</blockquote></details>


```python
# my code
# Time Complexity: O(lg n)
# Space Complexity: O(1)
def contains(ordered_list, number):
    start, end = 0, len(ordered_list) - 1

    while start <= end:
        mid = start + (end - start) // 2
        current = ordered_list[mid]

        if current == number:
            return True

        elif current > number:
            end = mid - 1

        elif current < number:
            start = mid + 1

    return False

```


## Inplace Shuffle
Дан массив чисел, нужно перетосавать массив в случайной порядке.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Получить случайный индекс.</li>
 <li>Заменить значение под текущим индексом на значение под случайным индексом.</li>
</ol>

</blockquote></details>


```python
# their solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):
    # If it's 1 or 0 items, just return
    if len(the_list) <= 1:
        return the_list

    last_index_in_the_list = len(the_list) - 1

    # Walk through from beginning to end
    for index_we_are_choosing_for in range(0, len(the_list) - 1):

        # Choose a random not-yet-placed item to place there
        # (could also be the item currently in that spot)
        # Must be an item AFTER the current item, because the stuff
        # before has all already been placed
        random_choice_index = get_random(index_we_are_choosing_for, last_index_in_the_list)

        # Place our random choice in the spot by swapping
        if random_choice_index != index_we_are_choosing_for:
            the_list[index_we_are_choosing_for], the_list[random_choice_index] = \
                the_list[random_choice_index], the_list[index_we_are_choosing_for]

```


## Simulate 5-sided die
У тебя есть ф-ия для генерации случайного числа от 1 до 7, воспользуйтесь ей для реализации функции для генерации
случайного числа от 1 до 5.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Если результат после вызова ф-ии rand7() больше чем 5, то вызвать ф-ию еще раз.</li>
</ol>

</blockquote></details>


```python
# their solution
# Time Complexity: O(inf)
# Space Complexity: O(1)
def rand5():
    result = 7  # arbitrarily large
    while result > 5:
        result = rand7()
    return result

```
