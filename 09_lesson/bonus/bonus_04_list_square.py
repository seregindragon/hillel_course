def square_numbers(numbers: list) -> list:
    """
    Замінює кожне число у списку його квадратом.

    :param numbers: Список чисел.
    :return: Новий список з квадратами чисел.
    """
    result = []
    # Ваш код тут
    result = map(lambda x: x ** 2, numbers)
    result = list(result)

    return result


# Перевірка
assert square_numbers([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]
assert square_numbers([0, -1, -2, -3]) == [0, 1, 4, 9]
assert square_numbers([]) == []
