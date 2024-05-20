def calculator(num1: int, num2: int, operation: str) -> int | float:
    """
    Реалізує простий калькулятор для двох чисел.

    :param num1: Перше число.
    :param num2: Друге число.
    :param operation: Операція (додавання, віднімання, множення, ділення).
    :return: Результат операції.
    """
    if operation == 'add':
        result = num1 + num2
    elif operation == 'del':
        result = num1 - num2
    elif operation == 'mult':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    else:
        result = 0
    # Ваш код тут
    return result


# Перевірка

assert calculator(5, 3, '999') == 8
