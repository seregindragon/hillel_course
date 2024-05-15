def apply_operation(data: list[int], operation) -> list:
    res = []
    for element in data:
        res.append(operation(element))
    return res


def square(number: int) -> int:
    return number ** 2


def double(number: int) -> int:
    return number * 2


numbers = [1, 2, 3, 4, 5]

square_numbers = apply_operation(numbers, square)
double_numbers = apply_operation(numbers, double)

print(square_numbers)
print(double_numbers)
