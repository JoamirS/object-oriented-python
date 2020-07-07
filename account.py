
class Account:
    def __init__(self, number_account, cardholder_name, balance_account, limit_account=1000):
        print(f'Criando o objeto {self}')
        self.number_account = number_account
        self.cardholder_name = cardholder_name
        self.balance_account = balance_account
        self.limit_account = limit_account
