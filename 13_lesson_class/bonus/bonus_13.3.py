def calculate_square_area(side: int) -> int:
    return side*side

# Перевірка:
area = calculate_square_area(4)  # Очікуваний результат: 16
print(area)

area = calculate_square_area(-3)  # Очікуваний результат: AssertionError: Side must be a positive number
print(area)