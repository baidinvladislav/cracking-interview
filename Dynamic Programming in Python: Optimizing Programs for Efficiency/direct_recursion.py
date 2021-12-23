def func(str, n):
    if n > 0:
        print(str, "called func with n =", n)
        func("func", n - 1)


def main():
    func("main", 7)


main()
