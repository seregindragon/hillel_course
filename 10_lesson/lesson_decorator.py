def decorator(func):
    def wrapper(*args,**kwargs):
        print("Before func")
        return func(*args,**kwargs)
    return wrapper


#@decorator()
def say_whee(name):
    print("Say whee")
    return f"Hello {name}"

say = decorator(say_whee)
string = say_whee("Hello")

print(string)