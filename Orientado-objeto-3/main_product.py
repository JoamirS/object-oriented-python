from validation_product import Validation


class Product:
    def __init__(self, name_input, price_input):
        self.name_product = name_input
        self.price_product = price_input

    def discount_price(self, percentage_input):
        self.price_product = self.price_product - (self.price_product * (percentage_input / 100))

#   Getter
    @property
    def price_product(self):
        return self.price_product

#   Setter
    @price_product.setter
    def price_product(self, new_value):
        validated_price = Validation.validation_string_input(input_string=new_value)
        self.price_product = validated_price


object_one = Product('Shirt', 40)
object_one.discount_price(10)
print(object_one.price_product)

