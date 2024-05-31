def check_positive(value: int) -> int:
    if value <= 0:
        raise ValueError("Value must be positive")
    return value

# Перевірка:
try:
    check_positive(5)  # Очікуваний результат: (без виводу, так як немає помилки)
    print("Перевірка пройшла успішно: 5 є додатнім")
except ValueError as e:
    print(e)

try:
    check_positive(-3)  # Очікуваний результат: ValueError: Value must be positive
except ValueError as e:
    print(e)  # Виведе: ValueError: Value must be positive
