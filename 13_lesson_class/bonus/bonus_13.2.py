def safe_divide(a: int, b: int) -> float:
    try:
        result = a / b
    except ZeroDivisionError:
        result = float('inf')  # уникнення ділення на нуль
    return result

# Перевірка:
result = safe_divide(10, 2)
print(result)  # Очікуваний результат: 5

result = safe_divide(8, 0)
print(result)  # Очікуваний результат: "Error: Division by zero"

assert safe_divide(15, 3) == 5