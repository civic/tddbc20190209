from abc import ABCMeta, abstractmethod


class ProductInterface(metaclass=ABCMeta):
    @abstractmethod
    def is_target(self):
        pass


class Food(ProductInterface):
    def __init__(self, name):
        pass

    def is_target(self):
        return True


class NewsPaper(ProductInterface):
    def __init__(self, name):
        pass

    def is_target(self):
        return True


class Beverage(ProductInterface):
    def __init__(self, name):
        pass

    def is_target(self):
        return True


class Liquor(ProductInterface):
    def __init__(self, name):
        pass

    def is_target(self):
        return False


class Drug(ProductInterface):
    def __init__(self, name):
        pass

    def is_target(self):
        return False
