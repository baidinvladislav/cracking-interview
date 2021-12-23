def func1(str, n):
    if n > 0:
        print(str, "called func1 with n =", n)
        func2("func1", n - 1)


def func2(str, n):
    if n > 0:
        print(str, "called func2 with n =", n)
        func1("func2", n - 2)


def main():
    func1("main", 7)


main()
