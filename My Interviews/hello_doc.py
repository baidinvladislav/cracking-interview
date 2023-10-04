# People
# id, name, otdel_id
# 1, Nik, 1
# 2, Vova, 2
# 3, Dima, 1

# Otdel
# id, name
# 1, dev
# 2, market

people = People.objects.all().select_related('otdel')
for person in people:
    print(person.name)
    print(person.otdel.name)

# n = > [1..n]
# n % 3 = > Fizz
# n % 5 = > Buzz
# n % 3
# и
# 5 = > FizzBuzz


def solution(number):
    for number in range(1, n + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("Fizz")
        elif number % 3 == 0:
            print("Buzz")
        elif number % 5 == 0:
            print("FizzBuzz")


# n ^ 2
# n
# log n

"""Функции возвращают 'True', если все значения 'data' различны.
   Небходимо определить сложность функций от меньшего к большему"""


# T: O(n)
# S: O(n)
def is_unique_3(data):
    aset = set(data)
    return len(aset) == len(data)


# T: O(n^2)
# S: O(n)
def is_unique_1(data):
    for i in range(len(data)):
        if data[i] in data[i + 1:]:
            return False
    return True


# T: O(n log n)
# S: O(n)
def is_unique_2(data):
    copy = list(data)
    copy.sort()
    for i in range(len(data) - 1):
        if copy[i] == copy[i + 1]:
            return False
    return True
