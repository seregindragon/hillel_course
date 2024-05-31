class Cat:
    def __init__(self, name: str, age: int, bree: str):
        self.name = name
        self.age = age
        self.bree = bree

    def __str__(self):  # default show
        return f"Cat name: {self.name}, Age: {self.age}. Bree: {self.bree}"

    def __setattr__(self, key, value):
        print(f"Trying to set {key} ")
        self.__dict__[key] = value

    def __delattr__(self, item):
        print("remove")
        del self.__dict__[item]


cat = Cat("Barsik", 3, "home")

print(cat.name)
cat.type = 1
print(cat.type)


del cat.type
print(cat.type)