list_triple = []
list_fifve = []
for i in range(100):
    if i % 3 == 0:
        list_triple.append(i)
    if i % 5 == 0:
        list_fifve.append(i)


print(list_triple)
print(list_fifve)
set_triple = set(list_triple)
set_fifve = set(list_fifve)
print(set_triple.intersection(set_fifve))
