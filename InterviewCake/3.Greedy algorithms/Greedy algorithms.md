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


## In-Place Shuffle
