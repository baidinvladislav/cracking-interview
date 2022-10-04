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


## Product of All Other Numbers


## Cafe Order Checker


## In-Place Shuffle
