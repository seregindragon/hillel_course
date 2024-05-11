def sum_of_elements(*args, **kwargs):
    for arg in args:
        print(arg)

    for key, value in kwargs.items():
        print(key, value)


print(sum_of_elements(1, 2, 3, 4, number_1=1, number_2=2, number_3=3))