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


# Создаем фейковый файл с логами
fake_logs = [
    "2023-10-05 14:30:00 [INFO] Database connection established",
    "2023-10-05 15:45:20 [ERROR] SQL query failed",
    "2023-10-06 08:10:15 [INFO] User 'john' logged in",
]

with open('postgres_logs.txt', 'w') as log_file:
    for log in fake_logs:
        log_file.write(log + '\n')


from datetime import datetime


def transform_date(line):
    # Извлекаем дату и время из строки лога
    log_date_str = line[:19]
    # Преобразуем строку в объект datetime
    log_date = datetime.strptime(log_date_str, "%Y-%m-%d %H:%M:%S")
    # Форматируем дату и время в новый формат
    new_date_format = log_date.strftime("%d/%m/%Y %H:%M:%S")
    return new_date_format


input_filename = 'postgres_logs.txt'
output_filename = 'updated_logs.txt'

try:
    with open(input_filename, 'r') as input_file:
        lines = input_file.readlines()

    with open(output_filename, 'w') as output_file:
        for line in lines:
            new_date_format = transform_date(line)
            # Записываем строку с новым форматом даты в новый файл
            output_file.write(new_date_format + ' ' + line[20:])

    print(f"Логи были успешно обработаны и записаны в файл {output_filename}")

except FileNotFoundError:
    print("Файл не найден.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
