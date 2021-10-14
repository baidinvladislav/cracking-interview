class Queue:
    def __init__(self):
        self.items = []

    @property
    def is_empty(self):
        return self.items == []

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        return self.items.pop(0)

    @property
    def length(self):
        return len(self.items)
