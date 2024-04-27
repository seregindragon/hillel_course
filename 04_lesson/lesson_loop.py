# Loop for / while
n = 0
while n < 10:
    n += 1
    if n == 5:
        #continue skip step
        break # break the loop
    print(n)


first_list = [2, 4, 5, 6, 7]

i = 0
while i < len(first_list):
    print(first_list[i])
    i += 1

for elem in first_list:
    print(elem)

for elem in range(5):
    print("g")
else:
    print("end loop")