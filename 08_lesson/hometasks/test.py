sentence = "Quick brown fox"
temp = sentence.split(" ")
for i in range(len(temp)):
    print(temp[i])
    temp[i] = temp[i][::-1]



print(" ".join(temp))
