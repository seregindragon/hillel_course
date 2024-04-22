# lst = [1,2,"3",True ] # lst = list() inizializacia list
# print(lst[-1])

# lst.append() - add to list to end list
# lst.insert() - insert to list (вставка в это место)
# lst.remove(element) - remove element (not index) 1st find
# lst.pop(index) - remove element with index and return element
# del lst[index] - remove element with index
# len(list) - lenth list
# lst.extend() - extend list by other list or (lst + lst2)
# y = [3,4] *3
# print(y)

#y = x[:] copy list

x = [1, 2, 3, 4, 5]
x1 = [x[-1]]
x1.extend(x[:len(x) - 1])
print(x, "=>", x1)
