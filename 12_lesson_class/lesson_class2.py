class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B,C):
   ...

b = D()
print(D.__mro__)
b.show()