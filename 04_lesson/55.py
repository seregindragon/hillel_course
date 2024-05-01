list1 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

print(list1, "-> ", end="")
for j in range(list1.count(0)):
    list1.remove(0)
    list1.append(0)
else:
    print(list1)
