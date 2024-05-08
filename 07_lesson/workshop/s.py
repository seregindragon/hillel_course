import string


def letters_between_input(input_string: str) -> str:
    start, end = input_string.split("-")
    all_letters = string.ascii_letters
    start_index = all_letters.index(start)
    end_index = all_letters.index(end)
    return all_letters[start_index:end_index + 1]


if __name__ == "__main__":
    input_str = input("letter via '-':")
    assert letters_between_input(input_str), 'test1'


