from class_shopping_cart import Product, ShoppingCart

checkout = ShoppingCart()
product_one = Product('Camiseta', 50)
product_two = Product('iPhone', 10000)
product_three = Product('Cup', 15)

checkout.insert_product(product_one)
checkout.list_product()
