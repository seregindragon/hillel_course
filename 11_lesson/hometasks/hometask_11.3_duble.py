def is_even(number: int) -> bool:
    str1 = str(number)
    if int(str1[-1]) in [2, 4, 6, 8, 0]:
        return True
    else:
        return False


assert is_even(2494563894038**2) is True
assert is_even(1056897**2) is False
assert is_even(24945638940387**3) is False
print("OK")