
print("Welcome to my calc")
while True:
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

    if input("Is there anything else you need to count?(y/n):") == "n":
        break

print("Thanks for using my calculator, come back again.©Seregin")
