import codecs

html3 = ""
with codecs.open("draft.html", 'r', 'utf-8') as file:
    html = file.read()
    # print(html.count("<"))
    a = ""
    while html.count("<") > 0:
        # print(html.count("<"))
        start = html.find("<")
        end = html.find(">")
        for i in range(start, end + 1):
            a += html[i]
        html = html.replace(a, "")
        a = ""
with codecs.open("cleaned.txt", 'w', 'utf-8') as file2:
    file2.write(html)

with codecs.open("cleaned.txt", 'r', 'utf-8') as file:
    html2 = file.readline()
    while html2:
        if html2.strip() == "":
            html2 = file.readline()
            continue
        html3 += html2.strip()
        html3 += "\n"
        html2 = file.readline()

with codecs.open("cleaned.txt", 'w', 'utf-8') as file2:
    file2.write(html3)

print(html3)
# print(content, "end")

# print(a)
# print("B",b)

# while content.count(">") > 0:
#      start = content.find("<")
#      end = content.find(">")
# print(content)
#
# if content == "":
#     break
# if "<" not in content:
#     file2.write(content)

# while content.count(">") > 0:
#     start = content.find("<")
#     end = content.find(">")
# for i in range(start, end+1):
#     print(content[i])
