# Ваш код тут
class Rectangle:
    def __init__(self, side: int):
        self.side = side


class Square(Rectangle):
    def calculate_area(self):
        return self.side * self.side


# Перевірка:
square = Square(5)
assert square.calculate_area() == 25
