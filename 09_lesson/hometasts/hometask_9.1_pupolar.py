def popular_words(text: str, words: list) -> dict:
    list1 = text.lower().split()
    words = list(words)
    output_summary = {}

    for i in range(len(words)):
        output_summary[words[i]] = list1.count(words[i])
    return output_summary


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}
print('OK')
