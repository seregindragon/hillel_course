class Cat:
    def __init__(self, name: str, age: int, bree: str):
        self.name = name
        self.age = age
        self.bree = bree


    pows = 4

cat = Cat("Barsik", 3,  "home")

print(getattr(cat,"pows", None))
print(hasattr(cat,"pows"))

setattr(cat, "pows", 5) # cat.pows = 5
print(cat.pows)

cat2 = Cat("Barsik", 3,  "home")

dct = {"name": "Voland", "age": 5}
for key, value in dct.items():
    setattr(cat2, key, value)lesson.py

print(cat.name)
print(cat.age)
print(cat.bree)