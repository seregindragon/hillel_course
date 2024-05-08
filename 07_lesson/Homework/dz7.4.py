def common_elements():
    list_triple = []
    list_fifve = []
    for i in range(100):
        if i % 3 == 0:
            list_triple.append(i)
        if i % 5 == 0:
            list_fifve.append(i)
    set_triple = set(list_triple)
    set_fifve = set(list_fifve)
    result_set = set_triple.intersection(set_fifve)
    return result_set


if __name__ == "__main__":
    assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
