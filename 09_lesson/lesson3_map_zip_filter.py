numbers = [1, 2, 3, 4, 5]
sq2 = map(lambda x: x**2, numbers)
result = list(sq2)
print(result)


numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filters2 = filter(lambda x: x % 2 == 0, numbers2)
result2 = list(filters2)
print(result2)

ages = [21, 22, 23]
names = ["Andrey", "Alexandr", "Katya"]

zippd = zip(names, ages)
result3 = list(zippd)
print(result3)