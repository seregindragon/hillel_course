file = open("text.txt", "r")
content = file.read()
print(content)
file.close()

file = open("text.txt", "w") #change
file.write("test2")
file.close()

file = open("text.txt", "a") #addintion
file.write("test3")
file.close()

file = open("text.txt", "r")
content = file.read()
file.write("kjdhfkj")
print(content)
file.close()