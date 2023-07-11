# Инкапсуляция - это механизм, который ограничивает доступ к данным и методам класса.

class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Защищенный атрибут
        self.__balance = balance  # Приватный атрибут

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Недостаточно средств на счете")

    def get_balance(self):
        return self.__balance

my_account = BankAccount("123456", 1000)

print(my_account._account_number)  # 123456 - атрибут доступен (но не рекомендуется)

print(my_account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'
print(my_account.get_balance()) # 1000 - атрибут доступен через публичный метод
