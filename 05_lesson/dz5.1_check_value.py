import keyword
import string

string1 = input()
string_result = "TRUE"
if string1.startswith("__"):
    exit("False")
if string1[0].isdigit() or ' ' in string1:
    string_result = "FALSE"
    exit("False")

for i in string1:
    if i.isupper():
        string_result = "FALSE"
        exit("False")

for j in string.punctuation:
    if j == "_":
        continue
    elif j in string1:
        string_result = "FALSE"
        exit("False")

for f in keyword.kwlist:
    if f in string1 and "_" not in string1:
        string_result = "FALSE"
        exit("False")

print("It is: ", string_result)
