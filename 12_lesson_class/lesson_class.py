class Person:
    count = 0
    def __init__(self, name: str):
        self.name = name
        Person.count += 1

    def __new__(cls, *args, **kwargs):
        print("Creating new Personal object")
        instance = super().__new__(cls)
        return instance


    def print_name(self): #need object
        print(f"Hi, {self.name}")

    @staticmethod #not need object
    def send(address: str):
        print(f"send:{address}")

    @classmethod
    def get_count(cls):
        return cls.count


print(Person.get_count())
person = Person("Andriy")
person.print_name()
person.send("mail.com")

print(Person.get_count())

