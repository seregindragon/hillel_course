def add_decorator(number):
    """
    Реалізує декоратор, який змінює поведінку функції, додаючи до результату функції число.

    :param number: Число для додавання.
    :return: Декоратор для додавання числа до результату функції.
    """
    def decorator(func):
        def wrapped_function(*args, **kwargs):
            result = func(*args, **kwargs)
            return result + number
        return wrapped_function
    return decorator

@add_decorator(5)
def example_function(x):
    return x * 2

# Перевірка
assert example_function(2) == 9