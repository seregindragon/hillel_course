class Item:

    def __init__(self, name: str, price: int, description: str, dimensions: str) -> None:
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}, price: {self.price}"


class User:

    def __init__(self, name: str, surname: str, numberphone: str, batko: str) -> None:
        self.name = name
        self.surname = surname
        self.numberphone = numberphone
        self.batko = batko

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"


class Purchase:
    def __init__(self, user: User) -> None:
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item: object, cnt: int):
        self.products[item] = cnt

    def __str__(self) -> str:
        items_str = "\n".join([f"{item.name}: {cnt} pcs." for item, cnt in self.products.items()])
        return f"User: {self.user}\nItems:\n{items_str}"

    def get_total(self) -> int:
        return sum(item.price * cnt for item, cnt in self.products.items())


lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162", "Ivanovich")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
assert isinstance(cart.user, User) is True

assert cart.get_total() == 60
assert cart.get_total() == 60
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40
