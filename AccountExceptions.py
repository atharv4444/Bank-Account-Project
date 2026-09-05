from InvalidAmountException import InvalidAmountException
from InsufficientBalanceException import InsufficientBalanceException
from MinimumBalanceViolationException import (
    MinimumBalanceViolationException
)
from InactiveAccountException import InactiveAccountException
from InvalidPinException import InvalidPinException


class Account:

    # ===== Constants =====

    MIN_BALANCE_SAVINGS = 500.0
    MIN_BALANCE_CURRENT = 1000.0
    MIN_AGE = 18
    MIN_PIN = 1000
    MAX_PIN = 9999


    # ===== Constructor =====

    def __init__(
        self,
        accountNumber,
        name,
        age,
        initialBalance,
        accountType
    ):

        # Validate age
        if age < self.MIN_AGE:
            raise ValueError(
                f"Customer must be at least "
                f"{self.MIN_AGE} years old. "
                f"Provided: {age}"
            )

        # Validate account type
        if accountType not in ["Savings", "Current"]:
            raise ValueError(
                f"Account type must be 'Savings' or 'Current'. "
                f"Provided: {accountType}"
            )

        # Determine minimum balance
        if accountType == "Savings":
            minimumBalance = self.MIN_BALANCE_SAVINGS
        else:
            minimumBalance = self.MIN_BALANCE_CURRENT

        # Validate initial balance
        if initialBalance < minimumBalance:
            raise ValueError(
                f"{accountType} account requires minimum balance "
                f"of ₹{minimumBalance}. "
                f"Provided: ₹{initialBalance}"
            )

        # Initialize fields
        self.__accountNumber = accountNumber
        self.__name = name
        self.__age = age
        self.__balance = initialBalance
        self.__accountType = accountType
        self.__status = "Active"
        self.__pin = None


    # ===== Business Methods =====

    def deposit(self, amount):

        self.validateActive()

        if amount <= 0:
            raise InvalidAmountException(
                f"Deposit amount must be positive. "
                f"Provided: ₹{amount}"
            )

        self.__balance += amount


    def withdraw(self, amount, pin):

        # Check account status
        self.validateActive()

        # Check if PIN is set
        if not self.hasPin():
            raise InvalidPinException(
                "PIN not set for this account"
            )

        # Verify PIN
        if not self.verifyPin(pin):
            raise InvalidPinException(
                "Incorrect PIN"
            )

        # Check amount
        if amount <= 0:
            raise InvalidAmountException(
                f"Withdrawal amount must be positive. "
                f"Provided: ₹{amount}"
            )

        # Check sufficient balance
        if amount > self.__balance:
            raise InsufficientBalanceException(
                f"Insufficient balance. "
                f"Available: ₹{self.__balance}, "
                f"Requested: ₹{amount}"
            )

        # Check minimum balance
        remainingBalance = self.__balance - amount

        if remainingBalance < self.getMinimumBalance():

            raise MinimumBalanceViolationException(
                f"Cannot withdraw. Minimum balance of "
                f"₹{self.getMinimumBalance()} required. "
                f"Available after withdrawal: "
                f"₹{remainingBalance}"
            )

        # Deduct amount
        self.__balance -= amount


    # ===== Account Status Management =====

    def closeAccount(self):

        if self.__status == "Inactive":
            raise RuntimeError(
                "Account is already closed"
            )

        self.__status = "Inactive"


    def reopenAccount(self):

        if self.__status == "Active":
            raise RuntimeError(
                "Account is already active"
            )

        self.__status = "Active"


    # ===== PIN Management =====

    def setPin(self, pin):

        if pin < self.MIN_PIN or pin > self.MAX_PIN:
            raise ValueError(
                "PIN must be a 4-digit number"
            )

        self.__pin = pin


    def verifyPin(self, pin):

        return self.__pin == pin


    def hasPin(self):

        return self.__pin is not None


    # ===== Helper Methods =====

    def getMinimumBalance(self):

        if self.__accountType == "Savings":
            return self.MIN_BALANCE_SAVINGS

        return self.MIN_BALANCE_CURRENT


    def validateActive(self):

        if self.__status != "Active":

            raise InactiveAccountException(
                "Account is inactive. "
                "Please reopen the account or contact support."
            )


    # ===== Getters =====

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