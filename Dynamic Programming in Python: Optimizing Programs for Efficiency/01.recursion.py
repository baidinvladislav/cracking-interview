# direct recursion
def direct(str, n):
    if n > 0:
        print(str, "called direct with n =", n)
        direct("direct", n - 1)


# indirect recursion
def indirect(str, n):
    if n > 0:
        print(str, "called indirect with n =", n)
        indirect_1("indirect", n - 1)


def indirect_1(str, n):
    if n > 0:
        print(str, "called indirect_1 with n =", n)
        indirect("indirect_1", n - 2)


def main():
    direct("main", 7)
    indirect("main", 7)


main()
