repeat1 = "y"
print("Welcome to my calc")
while repeat1 == "y":
    x = int(input("enter x:"))
    y = int(input("enter y:"))
    pro = input("enter action' + - * / ':")

    if pro == "/":
        if y == 0:
            print("we can't do it action!!!")
        else:
            print("equals:", x, "/", y, "=", x / y)

    elif pro == "*":
        print("equals:", x, "*", y, "=", x * y)
    elif pro == "-":
        print("equals:", x, "-", y, "=", x - y)
    elif pro == "+":
        print("equals:", x, "+", y, "=", x + y)
    else:
        print("Wrong action - shutdown you pc!!!")

    repeat1 = input("Is there anything else you need to count?(y/n):")

print("Thanks for using my calculator, come back again. ©Seregin")
