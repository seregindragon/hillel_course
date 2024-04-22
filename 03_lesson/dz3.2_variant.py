lst = [12, 3, 4, 10]
lst2 = lst.copy()
if len(lst) != 0:
    lst2.insert(0, lst[-1])
    del lst2[-1]
else:
    print("list is null")

print(lst, "=>", lst2)
