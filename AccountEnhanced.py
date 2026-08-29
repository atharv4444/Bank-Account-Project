class AccountEnhanced:

    def __init__(self, accountNumber, name, age, initialBalance, accountType):

        # Age validation
        if age < 18:
            age = 18

        # Account type validation
        if accountType not in ["Savings", "Current"]:
            accountType = "Savings"

        # Minimum balance
        if accountType == "Savings":
            minimumBalance = 500
        else:
            minimumBalance = 1000

        if initialBalance < minimumBalance:
            initialBalance = minimumBalance

        # Store account data
        self.__accountNumber = accountNumber
        self.__name = name
        self.__age = age
        self.__balance = initialBalance
        self.__accountType = accountType
        self.__status = "Active"
        self.__pin = None

    # Deposit
    def deposit(self, amount):

        if self.__status == "Inactive":
            return False

        if amount <= 0:
            return False

        self.__balance += amount
        return True

    # Withdraw with PIN
    def withdraw(self, amount, pin):

        # Check account status
        if self.__status == "Inactive":
            return False

        # Check PIN
        if not self.verifyPin(pin):
            return False

        # Check valid amount
        if amount <= 0:
            return False

        # Determine minimum balance
        if self.__accountType == "Savings":
            minimumBalance = 500
        else:
            minimumBalance = 1000

        # Check minimum balance after withdrawal
        if self.__balance - amount < minimumBalance:
            return False

        self.__balance -= amount
        return True

    # Close account
    def closeAccount(self):

        if self.__status == "Inactive":
            return False

        self.__status = "Inactive"
        return True

    # Reopen account
    def reopenAccount(self):

        if self.__status == "Active":
            return False

        self.__status = "Active"
        return True

    # Set PIN
    def setPin(self, pin):

        # PIN must be exactly 4 digits
        if pin < 1000 or pin > 9999:
            return False

        self.__pin = pin
        return True

    # Verify PIN
    def verifyPin(self, pin):

        if self.__pin is None:
            return False

        return self.__pin == pin

    # Check whether PIN exists
    def hasPin(self):

        return self.__pin is not None

    # Getters
    def getAccountNumber(self):
        return self.__accountNumber

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getBalance(self):
        return self.__balance

    def getAccountType(self):
        return self.__accountType

    def getStatus(self):
        return self.__status

    # Setters
    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age