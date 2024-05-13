def add_one(some_list: list) -> list:
    list2 = []
    sum_digital = 0
    for i in range(len(some_list)):
        sum_digital += int(some_list[i]) * (10 ** (len(some_list) - i - 1))
    sum_digital += 1

    str1 = str(sum_digital)
    for i in range(len(str1)):
        list2.append(int(str1[i]))
    return list2


if __name__ == "__main__":
    assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5]
    assert add_one([9, 9, 9]) == [1, 0, 0, 0]
    assert add_one([0]) == [1]
    assert add_one([9]) == [1, 0]
print("ОК")
