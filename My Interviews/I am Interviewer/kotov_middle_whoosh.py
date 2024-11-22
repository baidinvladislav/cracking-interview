# 1) У вас есть список объектов, и вам нужно найти объект, чей атрибут соответствует заданному значению. 
# Для примера, в списке people требуется найти объект, где имя (name) равно "Charlie". 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


people = [
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35),
    Person("David", 25)
]


def choose_person(persons: list[Person], name: str) -> Optional[Person]:
    for person in persons:
        if person.name == name:
            return person
    return None


person = people.get(name, key=lambda p: p.name)


# 2) Пример кастомного итератора, который возвращает квадраты чисел от 1 до N:
class SquareIterator:
    def __init__(self, num):
        self.num = num
        self.current_num = 1

    def __iter__(self):
        return self
        
    def __next__(self):
        if self.current_num >= self.num:
            raise StopIteration()

        square = self.current_num ** 2
        self.current_num += 1
        return square


# Пример использования
for square in SquareIterator(5):
    print(square)




# 3) Реализовать декоратор для бесконечного ретрая:
def retry_forever(func):
    @functols.wraps
    def wrapper(*args, **kwargs):
        while True:
            try:
                res = func(*args, **kwargs)
            except Exception:
                time.sleep(1)

        return res
    return wrapper


@retry_forever
def unstable_function():
    import random
    if random.random() < 0.8:  # 80% вероятность выбросить исключение
        raise ValueError("Случайная ошибка")
    print("Успешно!")


# 4) Чему будет равно значение переменной count после исполнения кода?
count = 0


def inc():
    global count
    with threading.Lock:
        count += 1


threads = []
for i in range(100):
    thread = Thread(inc)
    threads.append(thread)


for t in threads:
    t.join()    


print(count)


# 5) написать SQL запросы для получения "?"
# user:
#   id: int
#   name: str

# book:
#   id: int
#   user_id: int

# author:
#   id: int
#   book_id: int

# 1 === SELECT user_id FROM book WHERE book.id = 1;
# book id = 1
# user_id = ?

# 2 === SELECT author_id FROM author WHERE author.book_id = 1;
# book id = 1
# author_id - ?

# 3 === SELECT u.name FROM book b JOIN user u ON b.user_id = u.id WHERE b.id = 1;
# book id = 1
# user.name - ?


# 6) выборка из большой таблицы
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    is_active = Column(Boolean)


engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=engine)
session = Session()

def fetch_active_users():
    count = session.query(User).filter(User.is_active == True).count()
    for offset in range(0, count, batch_size):
        query = session.query(User).filter(User.is_active == True).limit(batch_size).offset(offset)
        yield query.all()
