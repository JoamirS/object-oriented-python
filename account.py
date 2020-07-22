
class Account:
    def __init__(self, number_account, cardholder_name, balance_account, limit_account=1000):
        print(f'Criando o objeto {self}')
        self.__number_account = number_account
        self.__cardholder_name = cardholder_name
        self.__balance_account = balance_account
        self.__limit_account = limit_account
        self.__bank_code = '001'

    def account_statement(self):
        print(f"Saldo {self.__balance_account} do titular {self.__cardholder_name}")

    def deposit_money(self, value):
        self.__balance_account += value

    def __can_withdraw(self, amount_to_be_withdrawn):
        amount_available_to_withdraw = self.__balance_account + self.__limit_account
        return amount_to_be_withdrawn <= amount_available_to_withdraw

    def withdraw_money(self, value):
        if self.__can_withdraw(value):
            self.__balance_account -= value
        else:
            print(f'O valor {value} passou o limite.')

    def transfer_money(self, value, destiny):
        self.withdraw_money(value)
        destiny.deposit_money = destiny

    @property
    def number_account(self):
        return self.__number_account

    @property
    def cardholder_name(self):
        return self.__cardholder_name

    @property
    def balance_account(self):
        return self.__balance_account

    @property
    def limit_account(self):
        return self.__limit_account

    @limit_account.setter
    def limit_account(self, new_limit):
        self.__limit_account = new_limit

    @staticmethod
    def bank_code():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
