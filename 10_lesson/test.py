def counter(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(count)
        return func(*args, **kwargs)

    return wrapper

# Приклад використання
@counter
def example_function():
    print("Inside the function")

example_function()
example_function()
example_function()