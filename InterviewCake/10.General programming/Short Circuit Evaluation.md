<h2>Short Circuit Evaluation</h2>

Это стратегия, которую используют большинство языков программирования (включая Python 3.6), 
чтобы избежать ненужной работы. Например, скажем, у нас было такое условное выражение:

```python
if it_is_friday and it_is_raining:
    print("board games at my place!")

```

Допустим, it_is_friday ложно. Поскольку Python 3.6 сокращает вычисление, он не стал бы проверять значение it_is_raining 
— он знает, что в любом случае условие ложно, и мы не будем печатать приглашение на вечер настольных игр.

Мы можем использовать это в своих интересах. Например, скажем, у нас есть такая проверка:

```python
if friends['Becky'].is_free_this_friday():
    invite_to_board_game_night(friends['Becky'])

```

Вместо этого мы могли бы сначала подтвердить, что мы с Бекки все еще в хороших отношениях:
```python
if 'Becky' in friends and friends['Becky'].is_free_this_friday():
    invite_to_board_game_night(friends['Becky'])

```

Таким образом, если «Бекки» нет в друзьях, Python проигнорирует остальную часть условного выражения и не выдаст ошибку KeyError.
