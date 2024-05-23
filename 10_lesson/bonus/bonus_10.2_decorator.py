def repeat_decorator(repeat_count):
    """
    Реалізує декоратор, який повторює виклик функції задану кількість разів.

    :param repeat_count: Кількість повторень.
    :return: Декоратор для повторюваного виклику функції.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            global value
            print("before")
            for _ in range(repeat_count):
                value = func(*args, **kwargs)
            return value

        return wrapper

    return decorator

@repeat_decorator(3)
def example_function():
    print("Function called")

# Перевірка
assert example_function() is None