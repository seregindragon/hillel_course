class TemperatureValueError(Exception):
    """Custom exception for invalid temperature values."""
    pass


class TemperatureConverter:
    def convert_celsius_to_fahrenheit(self, celsius: int):
        # Перевірка на реальну температуру
        if celsius < -273.15:
            raise TemperatureValueError("Invalid temperature value")
        fahrenheit = (celsius * 9 / 5) + 32
        return fahrenheit


# Перевірка:
converter = TemperatureConverter()
result_1 = converter.convert_celsius_to_fahrenheit(25)  # Очікуваний результат: 77.0
print(result_1)

result_2 = converter.convert_celsius_to_fahrenheit(-300)  # Очікуваний результат: TemperatureValueError: Invalid temperature value
print(result_2)
