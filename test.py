def create_an_account(number_account, cardholder_name, balance_account, limit_account):
    account = {"Number": number_account, "Holder": cardholder_name, "Balance": balance_account, "Limit_credit": limit_account}
    return account


def cash_deposit(account, value):
    account["Balance"] += value


def withdraw_money(account, value):
    account["Balance"] -= value


def account_statement(account):
    print(f"O saldo é {account['Balance']}")
