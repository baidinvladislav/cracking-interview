# Array and string manipulation
+ [Merging Meeting Times](#merging-meeting-times)
+ [Reverse String in Place](#reverse-string-in-place)
+ [Reverse Words](#reverse-words)
+ [Merge Sorted Arrays](#merge-sorted-arrays)
+ [Cafe Order Checker](#cafe-order-checker)


## Merging Meeting Times
Дан массив интервалов, смержите пересекающиеся интервалы.
Вернуть массив смерженных интервалов.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Отсортировать инпут по первым элемента кортежа.</li>
 <li>Инициализировать старт и конец.</li>
 <li>Смержить интервалы, если они пересекаются.</li>
 <li>Добавить, в результат, если не пересекаются, обновить старт и конец.</li>
 <li>После завершения цикла добавить последний элемент в результат.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: [(1, 3), (2, 4)]
Output: [(1, 4)]

Example 2:
Input: [(5, 6), (6, 8)]
Output: [(5, 8)]

Example 3:
Input: [(1, 8), (2, 5)]
Output: [(1, 8)]
```

```python
# time: O(n log n) - because of sorting
# space: O(n) - in worse case will save all items
def merge_ranges(meetings):
    meetings.sort(key=lambda x: x[0])
    result = []
    start, end = meetings[0][0], meetings[0][1]
    for new_start, new_end in meetings[1:]:
        if end >= new_start:
            end = max(end, new_end)
        else:
            result.append((start, end))

            start = new_start
            end = new_end

    result.append((start, end))
    return result
```


## Reverse String in Place
Дан массив элементов, представленных строками.
Вернуть массив в обратном порядке (развернуть массив).

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Используем два указателя, один идет по строке с начала массива, другой с конца массива.</li>
 <li>Свапаем элементы под указателями, пока указатели не встретятся в середине.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: ['A', 'B', 'C', 'D', 'E']
Output: ['E', 'D', 'C', 'B', 'A']

Example 2:
Input: []
Output: []

Example 3:
Input: ['A']
Output: ['A']
```

```python

def reverse(list_of_chars):
    left, right = 0, len(list_of_chars) - 1
    while left < right:
        list_of_chars[left], list_of_chars[right] = list_of_chars[right], list_of_chars[left]

        left += 1
        right -= 1

    return list_of_chars
```


## Reverse Words
Дан массив элементов, представленных символами, которые образуют слова.
Вернуть массив в обратном порядке, сохранить читаемость слов.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Используем два указателя, один идет по строке с начала массива, другой с конца массива.</li>
 <li>Сначала развернем массив и получим отзеркаленный порядок элементов.</li>
 <li>Воспользуемся той же ф-ей, но уже развернем часть массива (каждое слово).</li>
</ol>

</blockquote></details>

```
Example 1:
Input: ['t', 'h', 'i', 'e', 'f', ' ', 'c', 'a', 'k', 'e']
Output: ['c', 'a', 'k', 'e', ' ', 't', 'h', 'i', 'e', 'f']

Example 2:
Input: ['o', 'n', 'e', ' ', 'a', 'n', 'o', 't', 'h', 'e', 'r', ' ', 'g', 'e', 't']
Output: ['g', 'e', 't', ' ', 'a', 'n', 'o', 't', 'h', 'e', 'r', ' ', 'o', 'n', 'e']

Example 3:
Input: ['r', 'a', 't', ' ', 't', 'h', 'e', ' ', 'a', 't', 'e', ' ', 'c', 'a', 't', ' ', 't', 'h', 'e']
Output: ['t', 'h', 'e', ' ', 'c', 'a', 't', ' ', 'a', 't', 'e', ' ', 't', 'h', 'e', ' ', 'r', 'a', 't']
```

```python
def reverse_words(array):
    swap(0, len(array) - 1, array)

    j = 0
    for i in range(len(array) + 1):
        if i == len(array) or array[i] == ' ':
            swap(j, i - 1, array)
            j = i + 1

    print(array)


def swap(start_idx, end_idx, array):
    while start_idx < end_idx:
        array[start_idx], array[end_idx] = array[end_idx], array[start_idx]

        start_idx += 1
        end_idx -= 1

```


## Merge Sorted Arrays
Дан массив элементов, представленных символами, которые образуют слова.
Вернуть массив в обратном порядке, сохранить читаемость слов.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Создать результирующий массив размером суммой двух входных массивов.</li>
 <li>Инициализировать счетчики текущих индексов для 3 массивов (два входящий и один результрирующий).</li>
 <li>Инвариант цикла: пока не заполнили весь результирующий массив.</li>
 <li>На каждой итерации проверяем что не дошли до конца входных массивов.</li>
 <li>Если первый массив не исчерпан и либо второй массив испчерпан или нужно добавить в результирующий массив элемент из первого массива, добавить элемент из первого массива, увеличить счетчик индекса первого массива.</li>
 <li>Иначе добавить элемент из второго массива, увеличить счетчик индекса второго массива.</li>
 <li>На каждой итерации увеличить текущий индекс результирующего массива.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: [], []
Output: []

Example 2:
Input: [], [1, 2, 3]
Output: [1, 2, 3]

Example 3:
Input: [5, 6, 7], []
Output: [5, 6, 7]

Example 4:
Input: [2, 4, 6], [1, 3, 7]
Output: [1, 2, 3, 4, 6, 7]

Example 5:
Input: [2, 4, 6, 8], [1, 7]
Output: [1, 2, 4, 6, 7, 8]
```

```python
def merge_lists(my_list, alices_list):
    result = [None] * (len(my_list) + len(alices_list))
    current_my_list_idx = current_alices_list_idx = current_result_idx = 0
    while current_result_idx < len(result):
        is_my_list_exhausted = current_my_list_idx == len(my_list)
        is_alices_list_exhausted = current_alices_list_idx == len(alices_list)
        if not is_my_list_exhausted and \
                (is_alices_list_exhausted or my_list[current_my_list_idx] < alices_list[current_alices_list_idx]):
            result[current_result_idx] = my_list[current_my_list_idx]
            current_my_list_idx += 1
        else:
            result[current_result_idx] = alices_list[current_alices_list_idx]
            current_alices_list_idx += 1

        current_result_idx += 1

    return result

```


## Cafe Order Checker
Дано три массива, последний является очередью заказов из двух массивов.
Вернуть True, если заказы были обработаны FIFO, в противном случае вернуть False.


<details><summary>Рекурсивное решение #1:</summary><blockquote>

<ol>
 <li>Базовый случай: итоговый массив заказов пуст.</li>
 <li>Рекурсия: если следующий обслуженный заказ был в массиве “на вынос”, продвинуться по массиву общих заказов, продвинуться по массиву заказов “на вынос”.</li>
 <li>Рекурсия: если следующий обслуженный заказ был в массиве “на месте”, продвинуться по массиву общих заказов, продвинуться по массиву заказов “на месте”.</li>
 <li>Вернуть False, если заказ не совпадает ни с одним массивом заказов, т.к. эта ситуация противоречит FIFO.</li>
</ol>

</blockquote></details>


<details><summary>Рекурсивное решение #2:</summary><blockquote>

<ol>
 <li>Принцип тот же, но из-за слайсинга мы получаем квадратичное время, использум индексы, вместо слайсов, тем самым уменьшаем затраты по времени до линейного.</li>
</ol>

</blockquote></details>


<details><summary>Итеративное решение:</summary><blockquote>

<ol>
 <li>Пройти по массиву всех заказов.</li>
 <li>Если массив “на вынос” не исчерпан и первым находится заказ из общего массива заказов, то инкрементируем счетчик индекса массива “на вынос”.</li>
 <li>Если массив “на месте” не исчерпан и первым находится заказ из общего массива заказов, то инкрементируем счетчик индекса массива “на месте”.</li>
 <li>Вернуть False, если заказ следуюзщий на обработку из общего массива заказов, не содержится ни в одном из массивов заказов.</li>
 <li>Вернуть True, если цикл прошел до конца весь массив итоговых заказов.</li>
</ol>

</blockquote></details>


```
Example 1:
Input: [1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6]
Output: True

Example 2:
Input: [1, 5], [2, 3, 6], [1, 2, 6, 3, 5]
Output: False

Example 3:
Input: [], [2, 3, 6], [2, 3, 6]
Output: True

Example 4:
Input: [1, 5], [2, 3, 6], [1, 6, 3, 5]
Output: False

Example 5:
Input: [1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8]
Output: False

Example 6:
Input: [1, 9], [7, 8], [1, 7, 8]
Output: False

Example 7:
Input: [55, 9], [7, 8], [1, 7, 8, 9]
Output: False

Example 8:
Input: [27, 12, 18], [55, 31, 8], [55, 31, 8, 27, 12, 18]
Output: True
```

```python
# their third solution (iterative)
# Time complexity: O(n)
# Space complexity: O(1)
def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    take_out_orders_index = 0
    dine_in_orders_index = 0
    take_out_orders_max_index = len(take_out_orders) - 1
    dine_in_orders_max_index = len(dine_in_orders) - 1

    for order in served_orders:
        # If we still have orders in take_out_orders
        # and the current order in take_out_orders is the same
        # as the current order in served_orders
        if take_out_orders_index <= take_out_orders_max_index and order == take_out_orders[take_out_orders_index]:
            take_out_orders_index += 1

        # If we still have orders in dine_in_orders
        # and the current order in dine_in_orders is the same
        # as the current order in served_orders
        elif dine_in_orders_index <= dine_in_orders_max_index and order == dine_in_orders[dine_in_orders_index]:
            dine_in_orders_index += 1

        # If the current order in served_orders doesn't match the current
        # order in take_out_orders or dine_in_orders, then we're not serving first-come,
        # first-served.
        else:
            return False

    # Check for any extra orders at the end of take_out_orders or dine_in_orders
    if dine_in_orders_index != len(dine_in_orders) or take_out_orders_index != len(take_out_orders):
        return False

    # All orders in served_orders have been "accounted for"
    # so we're serving first-come, first-served!
    return True


# their second solution (recursive) without slicing so O(n) time instead of O(n^2)
# Time complexity: O(n)
# Space complexity: O(n)
def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders,
                               take_out_orders_index=0, dine_in_orders_index=0,
                               served_orders_index=0):
    # Base case we've hit the end of served_orders
    if served_orders_index == len(served_orders):
        return True

    # If we still have orders in take_out_orders
    # and the current order in take_out_orders is the same
    # as the current order in served_orders
    if ((take_out_orders_index < len(take_out_orders)) and
            take_out_orders[take_out_orders_index] == served_orders[served_orders_index]):
        take_out_orders_index += 1

    # If we still have orders in dine_in_orders
    # and the current order in dine_in_orders is the same
    # as the current order in served_orders
    elif ((dine_in_orders_index < len(dine_in_orders)) and
          dine_in_orders[dine_in_orders_index] == served_orders[served_orders_index]):
        dine_in_orders_index += 1

    # If the current order in served_orders doesn't match
    # the current order in take_out_orders or dine_in_orders, then we're not
    # serving in first-come, first-served order.
    else:
        return False

    # The current order in served_orders has now been "accounted for"
    # so move on to the next one
    served_orders_index += 1
    return is_first_come_first_served(
        take_out_orders, dine_in_orders, served_orders,
        take_out_orders_index, dine_in_orders_index, served_orders_index)


# their first solution (recursive)
# Time complexity: O(n^2)
# Space complexity: O(n^2)
def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):
    # Base case
    if len(served_orders) == 0:
        return True

    # If the first order in served_orders is the same as the
    # first order in take_out_orders
    # (making sure first that we have an order in take_out_orders)
    if len(take_out_orders) and take_out_orders[0] == served_orders[0]:
        # Take the first order off take_out_orders and served_orders and recurse
        return is_first_come_first_served(take_out_orders[1:], dine_in_orders, served_orders[1:])

    # If the first order in served_orders is the same as the first
    # in dine_in_orders
    elif len(dine_in_orders) and dine_in_orders[0] == served_orders[0]:
        # Take the first order off dine_in_orders and served_orders and recurse
        return is_first_come_first_served(take_out_orders, dine_in_orders[1:], served_orders[1:])

    # First order in served_orders doesn't match the first in
    # take_out_orders or dine_in_orders, so we know it's not first-come, first-served
    else:
        return False

```
