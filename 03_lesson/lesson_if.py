x = int(input("Enter number"))
y = int(input("Enter number"))

if y <= 0:
    y = int(input("enter y again:"))
elif y == 1:
    print("")
else:
    print("test")

p = x / y
print(p)

z = x if x > y else y
