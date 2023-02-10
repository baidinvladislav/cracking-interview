class A:
    def go(self):
        print("go A!")


class B(A):
    def go(self):
        super().go()
        print("go B!")


class C(A):
    def go(self):
        super().go()
        print("go C!")


class D(B, C):
    def go(self):
        super().go()
        print("go D!")


a = A()
b = B()
c = C()
d = D()


print(D.mro())
