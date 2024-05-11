def reverse_words(sentence: str) -> str:
    temp = sentence.split(" ")
    for i in range(len(temp)):
        print(temp[i])
        temp[i] = temp[i][::-1]

    return " ".join(temp)
