n1 = input().split(" ")
sum1 = 0
for i in range(len(n1)):
    if len(n1[i]) > sum1:
        sum1 = len(n1[i])

print(sum1)

