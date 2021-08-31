class ArrayList:
    def __init__(self, max_size=10):
        self.max_size = max_size
        self.list = [None] * self.max_size
        self.size = 0

    def add(self, val):
        if self.size >= self.max_size:
            self._increase_size()
        self.list[self.size] = val
        self.size += 1

    def _increase_size(self):
        new_max_size = self.max_size * 2
        new_list = [None] * new_max_size
        for i in range(0, self.max_size):
            new_list[i] = self.list[i]
        self.max_size = new_max_size
        self.list = new_list

    def get(self, index):
        if index >= self.size or index < 0:
            raise Exception('Invalid index')

        return self.list[index]

    # TODO: refactoring this method. It doesn't delete element
    def delete(self, index):
        if index >= self.size or index < 0:
            raise Exception('Invalid index')

        for i in range(index, self.size):
            self.list[index] = self.list[index+1]

        self.size -= 1


nums = ArrayList(max_size=1)

nums.add(1)
nums.add(2)
nums.add(3)
nums.add(4)

value = nums.get(1)

nums.delete(0)

print(nums.list)
