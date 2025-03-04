class Customer:
    def __init__(self, name: str, age: int, country: str):
        self.name: str = name
        self.age: int = age
        self.country: str = country


class ShoppingList:
    def __init__(self, owner: object):
        self.__owner: object = owner
        self.__items = []

    @property
    def owner(self):
        return self.__owner

    def __len__(self):
        return len(self.__items)

    def __getitem__(self, index):
        return self.__items[index]

    def add(self, item):
        if not item.can_be_sold_to(self.owner):
            raise ValueError()
        self.__items.append(item)


class Item:
    def __init__(self, name: str, price: int):
        self.price: int = price
        self.name: str = name

    def can_be_sold_to(self, owner: object):
        return True


class AgeRestrictedItem(Item):
    def __init__(self, name, price):
        super().__init__(name, price)

    def can_be_sold_to(self, owner: object):
        return owner.age >= 18


class CountryRestrictedItem(Item):
    def __init__(self, name, price):
        super().__init__(name, price)

    def can_be_sold_to(self, owner: object):
        return owner.country != "Arstotzka"
