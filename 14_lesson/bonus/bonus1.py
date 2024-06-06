class Print:
    def print_text(self, text: str) -> None:
        print(text)


class PrintToScreen(Print):
    def print_text(self, text: str) -> None:
        super().print_text(text)


# Ваш код тут
class PrintToFile(Print):
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def print_text(self, text: str) -> None:
        with open(self.filename, "w") as file:
            file.write(text)


# Ваш код тут

# Основний код
print_screen = PrintToScreen()
print_file = PrintToFile("output.txt")

print_screen.print_text("Hello, world!")
print_file.print_text("This text goes to a file.")
