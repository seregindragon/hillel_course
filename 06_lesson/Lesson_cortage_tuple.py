t = (1, ) #tuple
s = (1) #integer
t = tuple()

len(t) # medot lenth
#t[0] # element index = 0

# if in tuple we have list , list we can change

a = 10
b = 20

a, b = b, a

print("A:", a, "B:", b)

a2 = (1,2,3)
if 1 in a:
    print("True")
    