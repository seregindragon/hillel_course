class Cat:
    def __init__(self, _name: str, age: int, bree: str):
        self.__name = _name
        self.age = age
        self.bree = bree
    name = property()

    def __str__(self): #default show
        return f"Cat name: {self.__name}, Age: {self.age}. Bree: {self.bree}"


    @property
    def price(self):
        return 125






cat = Cat("Barsik", 3, "home")


print(cat.price)

