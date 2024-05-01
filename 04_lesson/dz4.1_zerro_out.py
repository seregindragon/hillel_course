list1 = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

print(list1, "-> ", end="")
for j in range(list1.count(0)):
    for i in range(len(list1)):
        if list1[i] == 0:
            list1.append(list1.pop(i))
else:
    print(list1)
