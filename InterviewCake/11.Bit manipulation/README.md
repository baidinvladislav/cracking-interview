# Bit manipulation
+ [The Stolen Breakfast Drone](#the-stolen-breakfast-drone)


## The Stolen Breakfast Drone
Дан массив чисел, все числа дубликаты, только одно число уникальное, вернуть уникальное число.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Применить оператор XOR для всех чисел массива в одной переменной.</li>
 <li>Вернуть переменную.</li>
</ol>

</blockquote></details>


```python
# their solution
# Time Complexity: O(n)
# Space Complexity: O(1)
def find_unique_delivery_id(delivery_ids):
    unique_delivery_id = 0

    for delivery_id in delivery_ids:
        unique_delivery_id ^= delivery_id

    return unique_delivery_id

```
