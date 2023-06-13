<h2>Мемоизация</h2>

Мемоизация гарантирует, что функция не будет запущено для одно и того же инпута более одного раза, сохраняя 
результат вычисления для конкретного инпута, обычно используется словарь.

Для примера рассмотрим простую рекурсивную функцию для вычисления числа Фибоначчи:\

```python
def fib(n):
    if n < 0:
        raise IndexError(
            'Index was negative. '
            'No such thing as a negative index in a series.'
        )
    
    elif n in [0, 1]:
        # Base cases
        return n
    
    print("computing fib(%i)" % n)
    return fib(n - 1) + fib(n - 2)
```

Наша функция запускается с одним и тем же инпутом несколько раз:
```python
>>> fib(5)
computing fib(5)
computing fib(4)
computing fib(3)
computing fib(2)
computing fib(2)
computing fib(3)
computing fib(2)
5
```

Мы можем представить рекурсивные вызовы нашей функции как дерево, где два потомка узла, это два рекурсивных вызова,
которые делает наша ф-ия:

```scss
                                      fib(5)
                      /                                 \
                    fib(4)                             fib(3)
                 /          \                         /     \
             fib(3)          fib(2)               fib(2)    fib(1)
             /    \         /     \              /     \
         fib(2)   fib(1)  fib(1)  fib(0)      fib(1)  fib(0)
        /     \
     fib(1)  fib(0)
```

Чтобы избежать повторной работы, вызванного ветвлением, мы можем обернуть функцию в класс с атрибутом memo, 
который сопставляет входные данные с имеющимся результатом вычисления. Тогда наш алгоритм будет улучшен.

1. Проверить словарик memo, чтобы узнать можем ли избежать вычисления ответа для заданного ввода 
2. Сохранить результаты вычисления в memo

```python
class Fibber(object):

    def __init__(self):
        self.memo = {}
    
    def fib(self, n):
        if n < 0:
            raise IndexError(
                'Index was negative. '
                'No such thing as a negative index in a series.'
            )
    
        # Base cases
        if n in [0, 1]:
            return n
    
        # See if we've already calculated this
        if n in self.memo:
            print("grabbing memo[%i]" % n)
            return self.memo[n]
    
        print("computing fib(%i)" % n)
        result = self.fib(n - 1) + self.fib(n - 2)
    
        # Memoize
        self.memo[n] = result
    
        return result
```

Благодаря данному подходу мы избежали повторных вызовов функции для одних и тех же аргументов:
```python
>>> Fibber().fib(5)
computing fib(5)
computing fib(4)
computing fib(3)
computing fib(2)
grabbing memo[2]
grabbing memo[3]
5
```

Теперь в нашем дереве рекурсии нет ни одного вызова с одинаковым аргументом более одного раза:
```scss
                                      fib(5)
                      /                                 \
                    fib(4)                             fib(3) // get from memo
                 /          \                         
             fib(3)          fib(2) // get from memo                
             /    \                     
         fib(2)   fib(1) // get from memo        
        /     \
     fib(1)  fib(0)
```

Мемоизация - это распространенная стратегия для задач на динамическое программирование, это задачи, решение которых состоит
из решений той же проблемы с меньшими входными данными (как в случае с задачей для нахождения чисел Фибоначчи).
Другая распространенная стратегия для задач на динамическое программирование это "bottom-up", которое получается обычно 
чистым и более эффективным.
