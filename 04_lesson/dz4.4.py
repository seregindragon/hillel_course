list1 = []
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        list1.append("FizzBuzz")
        continue
    elif i % 3 == 0:
        list1.append("Fizz")
        continue
    elif i % 5 == 0:
        list1.append("Buzz")
        continue
    else:
        list1.append(i)

print(list1)
