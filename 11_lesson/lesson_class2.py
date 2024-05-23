from abc import ABC, abstractmethod


class Animal(ABC):
    #_POWS = 4  # incosulacia only for the class
    @abstractmethod
    def speak(self):
        ...

class Dog(Animal):
    def __init__(self, age: int):
        self.__age = age

    def speak(self):
        super().speak()
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("may")


animal = Animal()
dog = Dog(12)
cat = Cat()

dog.speak()
cat.speak()
print(dog._Dog__age) #exclude not need use!!!