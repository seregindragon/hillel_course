lst = [12, 3, 4, 10, 8]

print(lst, end="")
print(" => ", end="")
if len(lst) > 0:
    a = lst.pop(-1)
    lst.insert(0, a)

print(lst, end="")
