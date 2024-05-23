def repeat(number):
    def decorator(func):
        def wrapper(*args, **kwargs):
            global value
            print("before")
            for _ in range(number):
                value = func(*args, **kwargs)
            return value

        return wrapper

    return decorator


@repeat(number=4)
def say_hello(name):
    print("hello!")
    return f"Hello {name}"


print(say_hello("And"))
