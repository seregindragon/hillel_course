def first_word(text: str) -> str:
    """ Пошук першого слова """
    text = text.replace(",", " ")
    text = text.replace(".", " ")
    text2 = text.split(" ")

    for word in text2:
        if "'" in word:
            temp = word.split("'")
            if temp[0].isalpha() and temp[1].isalpha():
                return word
        elif word.isalpha():
            return word


print(first_word("don't touch it"))
assert first_word("Hello world") == "Hello"
assert first_word("greetings, friends") == "greetings"
assert first_word("don't touch it") == "don't"
assert first_word(".., and so on ...") == "and"
assert first_word("hi") == "hi"
assert first_word("Hello.World") == "Hello"
print('OK')
