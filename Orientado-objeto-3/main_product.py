class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount_price(self, percentage):
        self.price = self.price - (self.price * (percentage / 100))

#   Getter
    @property
    def price_product(self):
        return self._price

#   Setter
    @price_product.setter
    def price_product(self, value):
        if isinstance(value, str):
            value = float(value.replace('R$', ''))

        self._price = value


object_one = Product('Shirt', 40)
object_one.discount_price(10)
print(object_one.price)
