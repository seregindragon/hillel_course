def facts(number: int) -> int:
    print(number)
    if number == 0 or number == 1:
        return 1
    else:
        return number * facts(number-1)


print(facts(4))