# Есть итерируемый объект A, надо проитерироваться по нему не используя цикл for и вывести каждый его элемент.
A = [1, 2, 3, 4, 5]
iterator = iter(A)

while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break

# Разработать класс MathList, который будет реализовывать структуру лист, но с индексацией с единицы. 
class MathList:
  def __init__(self, iterable=None):
      if iterable is None:
          self.data = []
      else:
          self.data = list(iterable)

  def __getitem__(self, index):
      if index < 1 or index > len(self.data):
          raise IndexError("Index out of range")
      return self.data[index - 1]

  def __setitem__(self, index, value):
      if index < 1 or index > len(self.data):
          raise IndexError("Index out of range")
      self.data[index - 1] = value

  def __len__(self):
      return len(self.data)

  def __repr__(self):
      return f"MathList({self.data})"

  def append(self, value):
      self.data.append(value)

  def insert(self, index, value):
      if index < 1 or index > len(self.data) + 1:
          raise IndexError("Index out of range")
      self.data.insert(index - 1, value)

  def remove(self, value):
      self.data.remove(value)

  def pop(self, index=-1):
      if index == -1:
          return self.data.pop()
      if index < 1 or index > len(self.data):
          raise IndexError("Index out of range")
      return self.data.pop(index - 1)

  def __iter__(self):
      return iter(self.data)

  def __contains__(self, value):
      return value in self.data

  def index(self, value):
      # Возвращает индекс с единицы, если элемент найден
      return self.data.index(value) + 1

  def count(self, value):
      return self.data.count(value)

  def extend(self, iterable):
      self.data.extend(iterable)


# что выведет в аутпут?
x = 10
y = x
y = 20
print(x)  # x все еще 10, потому что int неизменяемый объект


# что выведет в аутпут?
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4], потому что a и b ссылаются на один и тот же объект
