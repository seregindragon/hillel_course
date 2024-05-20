def factorial(num: int) -> int:
    """
    Обчислює факторіал числа num.

    :param num: Ціле число.
    :return: Факторіал числа num.
    """
    # Ваш код тут
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)


# Перевірка
assert factorial(5) == 120
