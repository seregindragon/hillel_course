import string


def is_palindrome(text: str) -> bool:
    str_temp = ""
    for i in text:
        if i not in string.punctuation:
            str_temp += i

    str_temp = str_temp.replace(" ", "").lower()
    if str_temp == str_temp[::-1]:
        return True

    return False


if __name__ == "__main__":
    assert is_palindrome('A man, a plan, a canal: Panama') is True
    assert is_palindrome('0P') is False
    assert is_palindrome('a.') is True
    assert is_palindrome('aurora') is False
print("ОК")
