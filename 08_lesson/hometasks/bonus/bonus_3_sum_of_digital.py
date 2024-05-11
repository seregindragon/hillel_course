def sum_of_digits(number: int) -> int:
    number = abs(number)
    sum_digital = 0
    print(len(str(number)))
    for i in range(len(str(number))):
        sum_digital += number % 10
        number //= 10

    return sum_digital