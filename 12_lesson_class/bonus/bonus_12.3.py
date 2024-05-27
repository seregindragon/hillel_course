class MathOperations:
    def __init__(self, digital1: int,digital2: int ) -> None:
        self.digital1 = digital1
        self.digital2 = digital2

    @staticmethod
    def multiply(digital1: int, digital2: int) -> int:
        return digital2 * digital1

# Перевірка:
assert MathOperations.multiply(3, 4) == 12