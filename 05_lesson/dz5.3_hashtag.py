import string

string1 = input("Enter string: ")
string3 = ""

for i in string1:
    if i not in string.punctuation:
        string3 += i


print("#" + string3[:139].title().replace(" ", ""))
