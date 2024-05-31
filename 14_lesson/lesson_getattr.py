class Cat:
    def __init__(self, name: str, age: int, bree: str):
        self.name = name
        self.age = age
        self.bree = bree

    def __str__(self): #default show
        return f"Cat name: {self.name}, Age: {self.age}. Bree: {self.bree}"

    # def __getattr__(self, item): # if attrible not exist
    #     return item

    def __getattribute__(self, item):
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        print(f"passed attr: {item}")




cat = Cat("Barsik", 3, "home")

print(cat.name)
print(cat.type)
