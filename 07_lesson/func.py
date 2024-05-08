def add_numbers(a, b): #if default value exmale b=3
    summ = a + b
    return summ


if __name__ == "__main__":
    print(add_numbers(1, 2))
    print(add_numbers(b=1, a=2))
