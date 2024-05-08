def second_index(text: str, some_str: str):
    if text.count(some_str) > 1:
        index_find = text.find(some_str, text.index(some_str) + 1)
        return index_find
    else:
        return None


if __name__ == "__main__":
    assert second_index("sims", "s") == 3
    assert second_index("find the river", "e") == 12
    assert second_index("hi", "h") is None
    assert second_index("Hello, hello", "lo") == 10
    assert second_index("Hello, hello", "llo") == 9
    print('ОК')
