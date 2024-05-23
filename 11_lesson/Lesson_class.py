class Car: #class
    wheels = 4 #atribut
    #def #metod
    def __init__(self, brand: str):
        self.brand = brand
    def start_engine(self, fuel: str):
        print(f"{self.brand}:  engine is launche with {fuel}!")

car_1 = Car("BWM") #object class
car_2 = Car("Mazda") #object class
car_1.start_engine("Diesel")
car_2.start_engine("GAS")

print(car_1.brand)
print(car_2.brand)
