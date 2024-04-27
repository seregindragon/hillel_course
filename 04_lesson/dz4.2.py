#list1 = [0, 1, 7, 2, 4, 8]
#list1 = [1, 3, 5]
#list1 = [6]
list1 = []
print(list1, "=> ", end="")
su = 0
if len(list1) > 0:
    for i in range(len(list1)):
        if i % 2 == 0:
            su += list1[i]
    else:
        print(su * list1[-1])
else:
    print("0")
