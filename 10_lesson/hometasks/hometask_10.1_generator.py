from inspect import isgenerator


def pow(x):
    return x ** 2


def some_gen(begin: int, end: int, func):
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """
    count = 0
    while count < end:
        yield begin
        begin = func(begin)
        count += 1


gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True
assert list(gen) == [2, 4, 16, 256]
print('OK')
