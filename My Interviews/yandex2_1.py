'''

add(x) - add element `x` to the structure

get_unique() - return some element that is uniquely represented in the structure

delete(x) - remove element `x` from the structure



Необходимо реализовать структуру данных с тремя операциями:

Операция  Add(x) - добавить элемент

Операция  GetUnique() - вернуть какой-то элемент, который представлен в структуре только один раз (или null, если таких элементов нет).

Операция  Delete(x) - удалить ровно одно вхождение элемента x. Если элемента равного x в структуре нет, то в структуре ничего не меняется.

'''


# space: O(n)

class UniqueStorage:

    def __init__(self):

        self.storage = defaultdict(int)

        self.unique_items = set()

    # time: O(1)

    def add(self, x):

        self.storage[x] += 1

        if self.storage[x] == 1:

            self.unique_items.add(x)

        else:

            self.unique_items.remove(x)

    # time: O(1)

    def get_unique(self):

        if len(self.unique_items) > 0:
            result = self.unique_items.pop()

            self.unique_items.add(result)

            return result

            # time: O(1)

    def delete(self, x):

        if x in self.storage:

            self.storage[x] -= 1

            if self.storage[x] == 0:
                del self.storage[x]

                self.unique_items.remove(x)

            if self.storage[x] == 1:
                self.unique_items.add(x)


ds = UniqueStorage()

ds.add("a")

ds.add("a")

ds.add("b")

# {"a": 2, "b": 1}

# {"b"}

v

ds.get_unique()

# b

ds.get_unique()  # None

ds.delete("a")

# {"a": 1, "b": 1}

# {"b", "a"}


add("a")

# {"a": 2, "b": 1}


add("b")

delete("a")
