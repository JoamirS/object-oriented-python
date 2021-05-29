from product_class import Product
'''
Criando um mini programa de descontos de produtos
'''
input_user_name_product = str(input('Digite o nome do produto: ')).capitalize()
input_user_price_product = float(input('Digite o preço do produto: '))
input_user_discount = float(input('Digite o valor do desconto: '))

object_test = Product(name_input=input_user_name_product, price_input=input_user_price_product)
value_discount = Product.discount_price(price_product=input_user_price_product, percentage_input=input_user_discount)
new_value_with_discount = Product.new_price_with_discount(value_product=input_user_price_product, value_discount_price=value_discount)

print(f' O nome do produto é {object_test.name_product}')
print(f' O preço do produto é {object_test.price_product}')
print(f' O valor do desconto é {value_discount}')
print(f' O valor do produto com desconto é {new_value_with_discount}')
