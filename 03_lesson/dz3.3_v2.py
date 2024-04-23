lst = [1, 2, 3]
lst2 = []
l1 = len(lst) // 2 + 1
if len(lst) % 2 == 0 and len(lst) != 0:
    lst2.append(lst[:len(lst) // 2])
    lst2.append(lst[len(lst) // 2:])
else:
    lst2.append(lst[:l1])
    lst2.append(lst[l1:])

print(lst, "=>", lst2)
