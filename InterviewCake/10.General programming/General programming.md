# General programming
+ [Rectangular love](#rectangular-love)


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
