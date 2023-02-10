from collections import defaultdict


class MyDict(defaultdict):
    def __init__(self):
        super(MyDict, self).__init__()
        self.array = []

    def get(self, key):
        item = super(MyDict, self).get(key)
        if item is None:
            self.array.append(item)

        return item

    def missing_keys(self):
        return self.array


def solution():
    my_dict = MyDict()
    my_dict[1] = "string"

    print(my_dict.get(1))
    print(my_dict.get(2))

    return my_dict.missing_keys()
