name = "Kolya"
age = 25
height = 1.81

string = "%s is %d years old and %f meters tall" % (name, age, height)  # old style

string2 = "{NAME} is {AGE} years old and {HEIG} meters tall".format(NAME=name, AGE=age, HEIG=height)  # new style"
print(string)


string3 = f"{name} is {age} years old and {height} meters tall"
print(string3)