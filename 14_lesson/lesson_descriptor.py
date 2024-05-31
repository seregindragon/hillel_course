class Coordinate:
    def __init__(self):
        self.value = None

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = value

    def __delete__(self, instance):
        del self.value


class Point:
    x = Coordinate()
    y = Coordinate()


point = Point()
print(point.x, point.y)

point.x = 5
point.y = 10

print(point.x, point.y)