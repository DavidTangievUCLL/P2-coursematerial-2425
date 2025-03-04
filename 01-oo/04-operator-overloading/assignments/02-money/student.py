class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __add__(self, other: object):
        if self.currency == other.currency:
            return Money(self.amount + other.amount, self.currency)
        raise RuntimeError("Mismatched currencies")

    def __sub__(self, other: object):
        if self.currency == other.currency:
            return Money(self.amount - other.amount, self.currency)
        raise RuntimeError("Mismatched currencies")

    def __mul__(self, multiplier: int):
        return Money(self.amount * multiplier, self.currency)
