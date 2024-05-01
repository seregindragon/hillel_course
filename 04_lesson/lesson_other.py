import random
first_list = [2, 4, 5, 6, 7]

for i,j in enumerate(first_list): # index and value
    print(i, "=>", j)


x = range(5) # range(start, stop -1, step)
print(x)


for _ in range(100):
    #print(random.randint(1, 100)) random from 1 to 100
    #print(random.choice(first_list)) # randome element from list
    #random.shuffle(first_list) # shufle mix
    print(first_list)


