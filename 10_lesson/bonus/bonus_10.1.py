def counter(start):
    count = start

    def increment():
        nonlocal count  # Для доступу до локальної змінної внутрішньої функції
        count += 1
        return count

    return increment


counter1 = counter(0)
print(counter1())  # Вивід: 1
print(counter1())  # Вивід: 2

