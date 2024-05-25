import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    html_temp = ""
    with codecs.open(html_file, 'r', 'utf-8') as file:
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

    with codecs.open(result_file, 'w', 'utf-8') as file2:
        file2.write(html)

    with codecs.open(result_file, 'r', 'utf-8') as file:
        html = file.readline()
        while html:
            if html.strip() == "":
                html = file.readline()
                continue
            html_temp += html.strip()
            html_temp += "\n"
            html = file.readline()

    with codecs.open(result_file, 'w', 'utf-8') as file2:
        file2.write(html_temp)

    return


delete_html_tags('draft.html')
