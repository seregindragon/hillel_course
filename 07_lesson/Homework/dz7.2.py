def correct_sentence(text: str) -> str:
    if text[0].upper() != text[0] and text[-1] != ".":
        str1 = text[0].upper() + text[1:] + "."
    elif text[0].upper() == text[0] and text[-1] != ".":
        str1 = text + "."
    elif text[0].upper() != text[0] and text[-1] == ".":
        str1 = text[0].upper() + text[1:]
    else:
        str1 = text
    return str1


if __name__ == "__main__":
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("hello") == "Hello."
    assert correct_sentence("Greetings. Friends") == "Greetings. Friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hello my dead friend,need meet you") == "Hello my dead friend,need meet you."
    print('ОК')
