# для двух строк напишите метод, определяющий, является ли одна строка перестановкой другой


# TODO: do it problem
def check_strings(string1, string2):
	storage = {}
	for i in string1:
		for j in string2:

			if i == j:
				storage[i] = 1

	if len(storage) == len(string1) == len(string2):
		print(f'str: -{string1}- is str: -{string2}-')
		return True
	else:
		print(f'str: -{string1}- is not str: -{string2}-')
		return False


check_strings('Hello', 'loHel')
