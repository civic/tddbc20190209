from enum import Enum


class CategoryOf軽減税率(Enum):
    Food = True
    Beverage = True
    NewsPaper = True

    Liquor = False
    Drug = False
    QuasiDrug = False


class Tax(Enum):
    対象 = 1.08
    対象外 = 1.10


class Product:
    def __init__(self, name, category, unit_price):
        self.name = name
        self.category = category
        self.unit_price = unit_price

    def is_reducible(self):
        return self.category.value

    def amount(self):
        if self.category.value:
            return int(self.unit_price * Tax.対象.value)

        return int(self.unit_price * Tax.対象外.value)

    def subtotal(self, quantity):
        if self.category.value:
            return int(self.unit_price * quantity * Tax.対象.value)

        return int(self.unit_price * quantity * Tax.対象外.value)
