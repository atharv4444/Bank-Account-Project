class Account:

    def __init__(self, account_number, name, age, initial_balance, account_type):
        self.__account_number = account_number
        self.__name = name
        self.__age = age
        self.__balance = initial_balance
        self.__account_type = account_type
        self.__status = "Active"

    def deposit(self, amount):
        if amount <= 0:
            return False

        self.__balance += amount
        return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self.__balance:
            return False

        self.__balance -= amount
        return True

    # Getters
    def get_account_number(self):
        return self.__account_number

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_balance(self):
        return self.__balance

    def get_account_type(self):
        return self.__account_type

    def get_status(self):
        return self.__status

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age