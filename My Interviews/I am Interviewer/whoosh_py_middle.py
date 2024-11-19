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



# 2) Пример кастомного итератора, который возвращает квадраты чисел от 1 до N:
class SquareIterator:
    ...
        

# Пример использования
for square in SquareIterator(5):
    print(square)



# 3) Реализовать декоратор для бесконечного ретрая:
def retry_forever(func):
    ...


@retry_forever
def unstable_function():
    import random
    if random.random() < 0.8:  # 80% вероятность выбросить исключение
        raise ValueError("Случайная ошибка")
    print("Успешно!")


sleep(1) # follow-up
# 4) Чему будет равно значение переменной count после исполнения кода?
count = 0


def inc():
    global count
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

# 1 ===
# book id = 1
# user_id = ?

# 2 ===
# book id = 1
# author_id - ?

# 3 ===
# book id = 1
# user.name - ?


# 6) Оптимизировать большую выборку из большой таблицы
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
    query = session.query(User).filter(User.is_active == True)
    return query.all()
