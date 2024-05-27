class Customer:
    def __init__(self, account):
        self.account = account

    def get_account(self):
        """
        Повертає об'єкт рахунку користувача.
        """
        return self.account

    def get_balance(self):
        """
        Повертає баланс рахунку користувача.
        """
        return self.account.get_balance()

class Account:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        """
        Повертає баланс рахунку.
        """
        return self.balance

class Bank:
    def __init__(self, customer):
        self.customer = customer

    def get_customer(self):
        """
        Повертає об'єкт користувача банку.
        """
        return self.customer

    def get_customer_balance(self):
        """
        Повертає баланс рахунку користувача.
        """
        return self.customer.get_balance()


# Користування без прямого ланцюжка викликів
bank = Bank(Customer(Account(1000)))
balance = bank.get_customer_balance()
print(f"The balance is: {balance}")

# Або 
balance = bank.get_customer().get_balance()
print(f"The balance is: {balance}")