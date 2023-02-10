"""
Реализовать кэш декоратор
"""


def memoize(function):
    memo = {}

    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv

    return wrapper


@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(4)


"""
Вывести кол-во строк в файле

Есть файл там есть логи, перевести дату в новый формат, записать все в новый файл, вернуть новый файл
"""
