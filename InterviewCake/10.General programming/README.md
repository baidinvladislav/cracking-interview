# General programming
+ [Rectangular love](#rectangular-love)
+ [Temperature tracker](#temperature-tracker)


## Rectangular love
Даны два прямоугольника на оси координат, найти пересечение двух прямоугольников.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Рассмотрим пересечение прямогоульников как совпадение интервалов ширин и интервалов высот.</li>
 <li>Создадим ф-ию для мержа интервалов.</li>
 <li>Вызовем ф-ию сначала для интервалов ширин, затем для интервалов высот.</li>
 <li>Если интервалы не пересекаются вернем None.</li>
</ol>

</blockquote></details>


```python
# my solution
# Time Complexity: O(1)
# Space Complexity: O(1)
def merge_intervals(interval1, interval2):
    intervals = [interval1, interval2]

    if intervals[0][1] > intervals[1][0]:
        start = max(intervals[0][0], intervals[1][0])
        end = min(intervals[0][1], intervals[1][1]) - start
        return start, end


def find_rectangular_overlap(rect1, rect2):
    result_rect = {}

    width_interval1 = (rect1['left_x'], rect1['left_x'] + rect1['width'])
    width_interval2 = (rect2['left_x'], rect2['left_x'] + rect2['width'])

    height_interval1 = (rect1['bottom_y'], rect1['bottom_y'] + rect1['height'])
    height_interval2 = (rect2['bottom_y'], rect2['bottom_y'] + rect2['height'])

    width = merge_intervals(width_interval1, width_interval2)
    height = merge_intervals(height_interval1, height_interval2)
    if width and height:
        result_rect['left_x'], result_rect['width'] = width
        result_rect['bottom_y'], result_rect['height'] = height
    else:
        result_rect['left_x'] = result_rect['width'] = None
        result_rect['bottom_y'] = result_rect['height'] = None

    return result_rect

```



## Temperature tracker
Реализовать класс для измерения температуры. 
Методы:
* insert 
* get_max
* get_min
* get_mean
* get_mode


Все методы должны быть реализованы за оптимальное время.

<details><summary>Решение:</summary><blockquote>

<ol>
 <li>Если мы будем использовать паттерн just-in-time - когда мы выполняем вычисления по запросу пользователя, то мы получаем O(N) время в методах: get_min() и get_max().</li>
 <li>Если использовать паттерн ahead-of-time, когда вычисления выполняются заранее, а по запросу пользователя отдается предвычисленный результат, то удастся реализовать все методы за O(1).</li>
</ol>

</blockquote></details>


```python
# their solution
# Time Complexity: O(1)
# Space Complexity: O(1)
class TempTracker(object):

    def __init__(self):
        # For mode
        self.occurrences = [0] * 111  # List of 0s at indices 0..110
        self.max_occurrences = 0
        self.mode = None

        # For mean
        self.number_of_readings = 0
        self.total_sum = 0.0  # Mean should be float
        self.mean = None

        # For min and max
        self.min_temp = float('inf')
        self.max_temp = float('-inf')

    def insert(self, temperature):
        # For mode
        self.occurrences[temperature] += 1
        if self.occurrences[temperature] > self.max_occurrences:
            self.mode = temperature
            self.max_occurrences = self.occurrences[temperature]

        # For mean
        self.number_of_readings += 1
        self.total_sum += temperature
        self.mean = self.total_sum / self.number_of_readings

        # For min and max
        if temperature > self.max_temp:
            self.max_temp = temperature
        if temperature < self.min_temp:
            self.min_temp = temperature

    def get_max(self):
        return self.max_temp

    def get_min(self):
        return self.min_temp

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode

```
