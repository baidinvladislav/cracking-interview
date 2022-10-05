# Greedy algorithms
+ [Apple Stocks](#apple-stocks)
+ [Highest Product of 3](#highest-product-of-3)
+ [Product of All Other Numbers](#product-of-all-other-numbers)
+ [Cafe Order Checker](#cafe-order-checker)
+ [In-Place Shuffle](#in-place-shuffle)


## Apple Stocks
Найти максимальную прибыль от продажи акций, дан массив с ценами, индекс - время.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Отслеживаем переменные с минимальной ценой и максимальной прибылью.</li>
 <li>Итерируем массив.</li>
 <li>На каждой итерации обновляем минимальную цену.</li>
 <li>Считаем максимальную прибыль.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: [1, 5, 3, 2]
Output: 4

Example 2:
Input: [7, 2, 8, 9]
Output: 7

Example 3:
Input: [2, 10, 1, 4]
Output: 8

Example 4:
Input: [1, 6, 7, 9]
Output: 8
```

```python
# Time Complexity: O(n)
# Space Complexity: O(1)
def get_max_profit(stock_prices):
    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for i in range(1, len(stock_prices)):
        price = stock_prices[i]
        profit = price - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, price)

    return max_profit

```


## Highest Product of 3
Найти максимальное произведение из трех чисел массива.

<details><summary>Решение за линию:</summary><blockquote>

<ol>
 <li>Для решения задачи за линию, нужно ослеживать 5 перемнных (highest_product_of_3, highest_product_of_2, highest, lowest_product_of_2, lowest) во время прохода по массиву.</li>
 <li>Инициализируем переменные как: highest_product_of_3=произведение первых трех чисел, highest_product_of_2=произведение первых двух чисел, highest=максимум из первых двух чисел, lowest_product_of_2=произведение первых двух чисел, lowest=минимум из первых двух чисел.</li>
 <li>По мере прохода по массиву обновляем highest_product_of_3=максимум из (highest_product_of_3 OR current * highest_product_of_2 OR current * lowest_product_of_2).</li>
 <li>По мере прохода по массиву обновляем highest_product_of_2=максимум из (highest_product_of_2 OR current * highest OR current * lowest).</li>
 <li>По мере прохода по массиву обновляем lowest_product_of_2=минимум из (lowest_product_of_2 OR current * highest OR current * lowest).</li>
 <li>По мере прохода по массиву обновляем highest=максимум из (highest, current).</li>
 <li>По мере прохода по массиву обновляем lowest=минимум из (lowest, current).</li>
 <li>Вернуть highest_product_of_3.</li>
</ol>

</blockquote></details>

<details><summary>Брутфорс решение:</summary><blockquote>

<ol>
 <li>Тройной цикл.</li>
 <li>Перемножаем все рядом стоящие тройки чисел массива, ослеживая их максимум.</li>
</ol>

</blockquote></details>


```
Example 1:
Input: [1, 2, 3, 4]
Output: 24

Example 2:
Input: [6, 1, 3, 5, 7, 8, 2]
Output: 336

Example 3:
Input: [-5, 4, 8, 2, 3]
Output: 96

Example 4:
Input: [-10, 1, 3, 2, -10]
Output: 300

Example 5:
Input: [-5, -1, -3, -2]
Output: -6
```

```python
# my code based on their solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise ValueError('Less than 3 items!')

    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])

    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2 = list_of_ints[0] * list_of_ints[1]

    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    for i in range(2, len(list_of_ints)):
        current = list_of_ints[i]

        highest_product_of_3 = max(
            highest_product_of_3,
            current * highest_product_of_2,
            current * lowest_product_of_2
        )

        highest_product_of_2 = max(
            highest_product_of_2,
            current * highest,
            current * lowest
        )

        lowest_product_of_2 = min(
            lowest_product_of_2,
            current * highest,
            current * lowest
        )

        highest = max(highest, current)
        lowest = min(lowest, current)

    return highest_product_of_3


# my brute force solution
# Time Complexity: O(n**3)
# Space Complexity: O(1)
def highest_product_of_3(list_of_ints):
    result = float('-inf')
    for i in range(len(list_of_ints)):
        for j in range(i + 1, len(list_of_ints)):
            for y in range(j + 1, len(list_of_ints)):
                current_result = list_of_ints[i] * list_of_ints[j] * list_of_ints[y]
                result = max(result, current_result)
    return result

```


## Product of All Other Numbers
Найти максимальное произведение из трех чисел массива.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Создать массив размером со входной массив.</li>
 <li>Записать в созданный массив умножение всех префиксов числа.</li>
 <li>Перемножить с конца все постфиксы с префиками в результирующем массиве.</li>
</ol>

</blockquote></details>

```
Example 1:
Input: [1, 2, 3]
Output: [6, 3, 2]

Example 2:
Input: [8, 2, 4, 3, 1, 5]
Output: [120, 480, 240, 320, 960, 192]

Example 3:
Input: [6, 2, 0, 3]
Output: [0, 0, 36, 0]

Example 4:
Input: [4, 0, 9, 1, 0]
Output: [0, 0, 0, 0, 0]

Example 5:
Input: [-3, 8, 4]
Output: [32, -12, -24]

Example 6:
Input: [-7, -1, -4, -2]
Output: [-8, -56, -14, -28]
```

```python
# my code based on their solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def get_products_of_all_ints_except_at_index(int_list):
    n = len(int_list)
    if n < 2:
        raise Exception

    result = [None] * n

    tmp = 1
    for i in range(n):
        result[i] = tmp
        tmp *= int_list[i]

    tmp = 1
    for i in range(n - 1, -1, -1):
        result[i] *= tmp
        tmp *= int_list[i]

    return result

```


## Cafe Order Checker


## In-Place Shuffle
