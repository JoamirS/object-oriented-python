
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

    def transfer_money(self, value, destiny):
        self.withdraw_money(value)
        destiny.deposit_money = destiny

    def get_number_account(self):
        return self.__number_account

    def get_cardholder_name(self):
        return self.__cardholder_name

    def get_balance_account(self):
        return self.__balance_account

    def get_limit_balance(self):
        return self.__limit_account

    def set_limit_account(self, new_limit):
        self.__limit_account = new_limit
