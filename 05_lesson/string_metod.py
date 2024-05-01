string = "i 'like' Python "

print(string.upper())  #UP ALL LETERS
print(string.lower())  #all symbold are little


print(string.title()) # every start word big letter

print(string.swapcase()) #change big letter to small and small to big
print(string.strip()) #clear notreadebele symbole before start and end string
print(string.lstrip()) #clear notreadable symvole from left
print(string.rstrip()) #clear notreadable symvole from right

new_string = string.replace("PHP","Python",1) # replace

string2 = "i like dogs and cats"
array = string.split(",") # split
print(array)

array = ["I", "like", "Python"]
spring3 = " ".join(array) # join array to string.
print(spring3)

print(spring3.find("P",1,2)) # fist index
print(spring3.rfind("P", 2, 4 )) # find from right
print(spring3.count("P",1,2)) #count find

value = input("enter number:")
if not value.isdigit(): #check is digitals
    print("Error. We need numbers!")
else:
    print(f"you got {value} apples")

value.isalnum() # check letters

print(string.startswith("P"))
print(string.startswith("I"))
print(string.endswith("P"))
print(string.endswith("I"))
