from inspect import isgenerator


def func(begin: int) -> int:
    count = 0
    for i in range(1, begin + 1):
        if begin % i == 0:
            count += 1

    if count == 2:
        return begin


def prime_generator(end: int):
    for i in range(1, end + 1):
        temp = func(i)
        if temp is not None:
            yield temp


gen = prime_generator(11)
assert isgenerator(gen) is True
assert list(prime_generator(10)) == [2, 3, 5, 7]
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13]
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print('Ok')
