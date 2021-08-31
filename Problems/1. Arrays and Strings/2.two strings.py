# Write a function that determines that string1 is a permutation of string2


def check_strings(string1, string2):
	list1 = list(string1)

	try:
		for i in string2:
			list1.remove(i)

		if len(list1) > 0:
			return False
		else:
			return True

	except ValueError:
		return False


if __name__ == '__main__':
	test_cases = [
		('hello', 'lloeh'),
		('python', 'ypthon'),
		('zxc', 'abc'),
		('qwerty', 'ytrewq')
	]

	for case in test_cases:
		print(check_strings(case[0], case[1]))
