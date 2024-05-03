import string
string1 = input("enter 1st and laty leter [a-b]:")
print(string.ascii_letters[string.ascii_letters.index(string1[0]):string.ascii_letters.index(string1[-1])+1])
