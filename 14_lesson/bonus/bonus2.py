class Shape:
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length: int, width: int) -> None:
        self.length = length
        self.width = width

    def calculate_area(self) -> int:
        return self.length * self.width


# Ваш код тут

class Circle(Shape):
    def __init__(self, radius: int) -> None:
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2


# Ваш код тут

rectangle = Rectangle(4, 5)
circle = Circle(3)

print(f"Area of Rectangle: {rectangle.calculate_area()}")
print(f"Area of Circle: {circle.calculate_area()}")
