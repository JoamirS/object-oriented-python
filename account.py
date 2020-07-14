
class Account:
    def __init__(self, number_account, cardholder_name, balance_account, limit_account=1000):
        print(f'Criando o objeto {self}')
        self.__number_account = number_account
        self.__cardholder_name = cardholder_name
        self.__balance_account = balance_account
        self.__limit_account = limit_account

    def account_statement(self):
        print(f"Saldo {self.__balance_account} do titular {self.__cardholder_name}")

    def deposit_money(self, value):
        self.__balance_account += value

    def withdraw_money(self, value):
        self.__balance_account -= value

    def transfer_money(self, value, origin, destiny):
        origin.withdraw_money(value)
        origin.deposit_money = destiny
