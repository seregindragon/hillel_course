import random

list1 = []
list2 = []
for i in range(random.randint(3, 10)):
    list1.append(random.randint(0, 10))
else:
    print(list1, "=> ", end="")

for j in 0, 2, -2:
    list2.append(list1[j])
else:
    print(list2)
