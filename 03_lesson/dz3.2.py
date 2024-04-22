lst = [12]
lst2 = []
if len(lst) != 0:
    lst2.append(lst[-1])
    lst2.extend(lst[:len(lst)-1])
else:
    print('list is null')
print(lst, "=>", lst2)
