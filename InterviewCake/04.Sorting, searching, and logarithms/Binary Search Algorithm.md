<h2>Алгоритм бинарного поиска</h2>
Алгоритм бинарного поиска ищет элемент в отсортированном массиве за O(lg(n)).
Брутфорс ищет элемент, проходя по всем элементам массива за O(n) в худшем случае.

Пусть у нас есть отсортированный массив. Чтобы воспользоваться бинарным поиском, нам необходимо:
1. Начать с элемента по середине массива: он больше или меньше искомого элемента? Поскольку наш список отсортирован,
это может сказать нам с левой стороны или с правой стороны от центрального элемента находится искомый элемент.
2. Мы эффективно разделили проблему на попалам. Мы можем исключить ту половину, в которой точно не будет находиться
наш искомый элемент.
3. Повторить те же действия пока не найдем искомый элемент или не исчерпаем весь массив.

Бинарный поиск можно реализовать как рекурсивно, так и итеративно, вот итеративная версия:

```python
def binary_search(target, nums):
    """See if target appears in nums"""

    # We think of floor_index and ceiling_index as "walls" around
    # the possible positions of our target, so by -1 below we mean
    # to start our wall "to the left" of the 0th index
    # (we *don't* mean "the last index")
    floor_index = -1
    ceiling_index = len(nums)

    # If there isn't at least 1 index between floor and ceiling,
    # we've run out of guesses and the number must not be present
    while floor_index + 1 < ceiling_index:

        # Find the index ~halfway between the floor and ceiling
        # We use integer division, so we'll never get a "half index"
        distance = ceiling_index - floor_index
        half_distance = distance // 2
        guess_index = floor_index + half_distance

        guess_value = nums[guess_index]

        if guess_value == target:
            return True

        if guess_value > target:
            # Target is to the left, so move ceiling to the left
            ceiling_index = guess_index
        else:
            # Target is to the right, so move floor to the right
            floor_index = guess_index

    return False

```

Откуда мы знаем, что алгоритм бинарного поиска работает за O(lg(n))?
Единственная не постоянная вещь в алгоритме - это количество итераций нашего цикла. На каждом шаге наш цикл
укорачивает входной массив ровно на половину. До тех пор пока в массиве не останется всего один элемент.

Вопрос, в том сколько раз необходимо поделить изначальный размер массива - n, на половину, чтобы получить 1?

n * 1/2 * 1/2 * 1/2 * 1/2 * ... = 1

Как много 1/2 здесь? Мы не знаем еще, но мы можем взять это число за Х:
n (1/2) ^ х = 1

Теперь мы можем вычислить его:
n * (1/2) ^ x = 1
n/(2 ^ n) = 1
n = 2^x

Теперь можно вычислить х через логарифм. log10 = 100, означает, сколько раз нужно умножить 10, чтобы получить 100?
Ответ 2.

В таком случае, если у нас есть log2 с обоих сторон:
log2n = log2(2) ^ x

Правая часть справшивает нас, какая сила может превратить 2 в 2^x? Ответ будет х.
log2n = x

Количество раз, которыми мы делим входной массив на половину, чтобы получить 1 элемент это log2n.
Так что общие затраты будут равняться O(lg(n)).

Осторожно: мы можем использовать бинарный поиск, только если наш входной массив отсортирован.
