lst = [1, 2, 3]
lst2 = []

if len(lst) % 2 == 0 and len(lst) != 0:
    lst2.append(lst[:len(lst) // 2])
    lst2.append(lst[len(lst) // 2:])
elif len(lst) % 2 != 0 and len(lst) != 0:
    lst2.append(lst[:len(lst) // 2 + 1])
    lst2.append(lst[len(lst) // 2 + 1:])
elif len(lst) == 0:
    lst2.append([])
    lst2.append([])

print(lst, "=>", lst2)
