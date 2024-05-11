def example(posisional, named, *args, **kwargs):
    print(f"Positional: {posisional}")
    print(f"Namde: {named}")
    print(f"add: {args}")
    print(f"add named: {kwargs}")

example("7",named=9, mas=1)