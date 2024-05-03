digital_get = input("Enter digital:")
digital_change = 1
while True:
    for i in digital_get:
        digital_change *= int(i)

    else:
        digital_get = str(digital_change)
        digital_change = 1

    if int(digital_get) <= 9:
        break
