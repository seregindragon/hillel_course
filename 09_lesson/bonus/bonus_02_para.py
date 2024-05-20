def multiply_even_numbers(numbers:list) -> list:
    """
    Помножує всі парні числа у списку на 2.

    :param numbers: Список чисел.
    :return: Новий список з парними числами, помноженими на 2.
    """
    result = []
    filters2 = filter(lambda x: x % 2 == 0, numbers)
    fil_res = list(filters2)
    for i in range(len(fil_res)):
        result.append(fil_res[i] * 2)

    # Ваш код тут
    return result

# Перевірка
assert multiply_even_numbers([1, 2, 3, 4, 5, 6]) == [4, 8, 12]