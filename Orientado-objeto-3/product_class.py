from validation_product import Validation


class Product:
    def __init__(self, name_input, price_input):
        self.__name_product = name_input
        self.__price_product = price_input
        self.validation_string = False

#   Getter
    @property
    def name_product(self):
        return self.__name_product

#   Getter
    @property
    def price_product(self):
        return self.__price_product

#   Setter
    @price_product.setter
    def price_product(self, new_value):
        self.__price_product = new_value

    @staticmethod
    def discount_price(price_product, percentage_input):
        discount_price_product = (price_product * percentage_input) / 100
        return discount_price_product

    @staticmethod
    def new_price_with_discount(value_product, value_discount_price):
        new_price_product = value_product - value_discount_price
        return new_price_product
