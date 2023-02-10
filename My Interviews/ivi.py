# sys.getsizeof(str()) == sys.getsizeof(list())
# sys.getsizeof(list()) > sys.getsizeof(set())
# sys.getsizeof(tuple()) == sys.getsizeof(list())
# sys.getsizeof(float()) > sys.getsizeof(int())

# str < list
# list < set
# tuple < list
# float == int


# ================================


def foo(i):
    pass


d = {
    1: '1',
    'two': '2',
    (3, 3): '3',
    foo: [1, 1]
}

print(''.join([
    d[1],
    d['two'],
    d[(3, 3)],
    d[[4, 4]],  # error
    d[foo],
    d[{6: 6}]  # error
]))


# ================================


def gen():
    counter = 0
    while True:
        yield counter
        counter += 1


print([i for i in gen()][:6])
# [0, 1, 2, 3, 4, 5]

print([i for i in gen() if i < 6])
# [0, 1, 2, 3, 4, 5]

print((i for i in gen())[:6])
# 0


# ==================
c = 1


def f(n):
    return c + n  # 2


def g(n):
    c = c + n
    return c


print(f(1))  # 2
print(g(2))  # 4


# ===============

class User(models.Model):
    id = int


class Book(model.Model):
    id = int
    user_id = IntegerField(related_name='books')


user = User.objects.get(id=1)

# 9
for book in user.books.select_related().all():
    pass

# ====================================

# user:
# id: int
# name: str
#
# book:
# id: int
# user_id: int
#
# author:
# id: int
# book_id: int

# book id = 1
# select
# user_id
# from book where
# book.id = 1;

# book id = 1
# author id - ?
# select
# author.id
# from author where
# book_id = 1;

# book id = 1
# user.name - ?
# select
# user.name, book.id
# from book
# left join user on book.user_id = user.id where book.id = 1;
