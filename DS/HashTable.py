class HashTable:
	def __init__(self):
		self.MAX = 100
		self.container = [None for i in range(self.MAX)]

	def hash_func(self, key):
		hash_value = 0
		for char in key:
			hash_value += ord(char)
		return hash_value % self.MAX

	def add(self, key, value):
		hash_value = self.hash_func(key)
		self.container[hash_value] = value

	def get(self, key):
		hash_value = self.hash_func(key)
		return self.container[hash_value]


ht = HashTable()
ht.add('name', 'Alex')

print(ht.get('name'))
