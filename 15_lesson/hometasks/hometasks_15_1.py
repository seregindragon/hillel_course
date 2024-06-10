class Rectangle:

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.get_square() == other.get_square()
        return False

    def __add__(self, other):
        if isinstance(other, Rectangle):
            square2 = self.get_square() + other.get_square()
            width2 = self.width
            height2 = square2 / width2
            return Rectangle(width2, height2)
        return None

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            square2 = self.get_square() * n
            width2 = self.width
            height2 = square2 / width2
            return Rectangle(width2, height2)
        return None

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
assert r1.get_square() == 8
assert r2.get_square() == 18

r3 = r1 + r2
assert r3.get_square() == 26

r4 = r1 * 4
assert r4.get_square() == 32

assert Rectangle(3, 6) == Rectangle(2, 9)
