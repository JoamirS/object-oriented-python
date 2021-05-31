class ShoppingCart:
    def __init__(self):
        self.products = []

    def insert_product(self, product):
        self.products.append(product)

    def list_product(self):
        for product in self.products:
            print(product.name, product.price)

    def total_sum(self):
        total = 0
        for product in self.products:
            total += product.value
        return total


class Product:
    def __init__(self, name_input, value_input):
        self.name = name_input
        self.price = value_input

