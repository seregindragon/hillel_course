x = int(input("enter x:"))
y = int(input("enter y:"))
pro = input("enter action' + - * / ':")

if pro == "/":
    if y == 0:
        y = int(input("Enter 'y' again but more 0:"))
    elif y < 0:
        y = int(input("Enter 'y' again but more 0:"))
    print("equals:", x, "/", y, "=", x / y)
elif pro == "*":
    print("equals:", x, "*", y, "=", x * y)
elif pro == "-":
    print("equals:", x, "-", y, "=", x - y)
elif pro == "+":
    print("equals:", x, "+", y, "=", x + y)
else:
    print("Wrong action - shutdown you pc!!!")
