lst = [1, 2, 3]
lst2 = []

if len(lst) % 2 == 0:
    l1 = len(lst) //2
    lst2.append(lst[:l1])
    lst2.append(lst[l1:])
else:
    l1 = len(lst) // 2 +1
    lst2.append(lst[:l1])
    lst2.append(lst[l1:])

print(lst, "=>", lst2)
