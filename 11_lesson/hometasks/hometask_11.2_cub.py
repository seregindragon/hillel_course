from inspect import isgenerator


def generate_cube_numbers(end: int):
    for i in range(2, end + 1):
        if i ** 3 > end:
            return
        else:
            yield i ** 3


gen = generate_cube_numbers(1)
assert isgenerator(gen) is True
assert list(generate_cube_numbers(10)) == [8]
assert list(generate_cube_numbers(100)) == [8, 27, 64]
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000]
print("OK")
