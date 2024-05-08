text = "Hello, hello"
find_text = "lo"

if text.count(find_text) > 1:
    print(text.find(find_text, text.index(find_text)+1))
else:
    print(None)