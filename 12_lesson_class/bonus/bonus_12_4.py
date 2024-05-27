class A:
    def show(self):
        print("A")


class B(A):
    def show(self):
        print("B")


class C(A):
    def show(self):
        print("C")


class D(B, C):
    def show(self):
        print("D")


obj_A = A()
output_A = capture_stdout(obj_A.show)
assert output_A == "A"
