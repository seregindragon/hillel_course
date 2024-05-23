def closure_example(x):
    prev_x = x
    def inner_function(y):
        nonlocal prev_x  # Вказуємо, що змінюємо змінну prev_x відносно замикання
        result = prev_x + y  # Результат - попереднє значення x плюс нове значення y
        prev_x = result  # Зберігаємо результат як нове попереднє значення x для наступного виклику
        return result

    return inner_function


# Створення замикання з початковим значенням 10
closure_instance = closure_example(5)



# Перевірка
assert closure_instance(3) == 8