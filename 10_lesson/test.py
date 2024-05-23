def counter(func):
    count = 0


    def increment():
        nonlocal count  # Для доступу до локальної змінної внутрішньої функції
        count += 1
        return count


    return increment


@counter
def example_function():
    print("Inside the function")