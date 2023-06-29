<h2>Mutable vs Immutable Objects</h2>

Изменяемый объект может быть изменен после его создания, а неизменяемый объект — нет. 
Например, списки в Python изменяемы:

```python
int_list  = [4, 9]

int_list[0] = 1
# int_list is now [1, 9]

```

А кортежи неизменны:
```python
int_tuple = (4, 9)

int_tuple[0] = 1
# Raises: TypeError: 'tuple' object does not support item assignment

```

Строки могут быть изменяемыми или неизменяемыми в зависимости от языка.

Строки неизменяемы в Python:

```python
test_string = 'mutable?'

test_string[7] = '!'
# Raises: TypeError: 'str' object does not support item assignment

```

Но в некоторых других языках, таких как Ruby, строки изменяемы:

Изменяемые объекты хороши тем, что вы можете вносить изменения на месте, не выделяя новый объект. 
Но будьте осторожны: всякий раз, когда вы вносите изменения в объект, все ссылки на этот объект теперь будут отражать изменение.
