from abc import ABC, abstractmethod

from InvalidAmountException import InvalidAmountException
from InsufficientBalanceException import InsufficientBalanceException
from MinimumBalanceViolationException import MinimumBalanceViolationException
from InactiveAccountException import InactiveAccountException
from InvalidPinException import InvalidPinException


class Account(ABC):

    # ===== Constants =====

    MIN_AGE = 18
    MIN_PIN = 1000
    MAX_PIN = 9999

    # ===== Abstract Methods =====

    @abstractmethod
    def getMinimumBalance(self):
        pass

    @abstractmethod
    def getAccountType(self):
        pass

    # ===== Constructor =====

    def __init__(self, accountNumber, name, age, initialBalance):

        # Validate age
        if age < self.MIN_AGE:
            raise ValueError(
                f"Customer must be at least "
                f"{self.MIN_AGE} years old. "
                f"Provided: {age}"
            )

        # Get minimum balance from child class
        minimumBalance = self.getMinimumBalance()

        # Validate minimum balance
        if initialBalance < minimumBalance:
            raise ValueError(
                f"{self.getAccountType()} account requires "
                f"minimum balance of ₹{minimumBalance}. "
                f"Provided: ₹{initialBalance}"
            )

        # Initialize fields
        self.accountNumber = accountNumber
        self.name = name
        self.age = age
        self.balance = initialBalance
        self.status = "Active"
        self.pin = None

    # ===== Business Methods =====

    def deposit(self, amount):

        self.validateActive()

        if amount <= 0:
            raise InvalidAmountException(
                f"Deposit amount must be positive. "
                f"Provided: ₹{amount}"
            )

        self.balance += amount

    def withdraw(self, amount, pin):

        self.validateActive()

        self.validatePin(pin)

        self.validateAmount(amount)

        if amount > self.balance:
            raise InsufficientBalanceException(
                f"Insufficient balance. "
                f"Available: ₹{self.balance}, "
                f"Requested: ₹{amount}"
            )

        newBalance = self.balance - amount

        if newBalance < self.getMinimumBalance():
            raise MinimumBalanceViolationException(
                f"Cannot withdraw. "
                f"Minimum balance of ₹{self.getMinimumBalance()} "
                f"required. "
                f"Available after withdrawal: ₹{newBalance}"
            )

        self.balance = newBalance

    # ===== Account Status Management =====

    def closeAccount(self):

        if self.status == "Inactive":
            raise RuntimeError(
                "Account is already closed"
            )

        self.status = "Inactive"

    def reopenAccount(self):

        if self.status == "Active":
            raise RuntimeError(
                "Account is already active"
            )

        self.status = "Active"

    # ===== PIN Management =====

    def setPin(self, pin):

        if pin < self.MIN_PIN or pin > self.MAX_PIN:
            raise ValueError(
                "PIN must be a 4-digit number"
            )

        self.pin = pin

    def verifyPin(self, pin):

        return self.pin == pin

    def hasPin(self):

        return self.pin is not None

    # ===== Helper Methods =====

    def validateActive(self):

        if self.status != "Active":
            raise InactiveAccountException(
                "Account is inactive. "
                "Please reopen the account or contact support."
            )

    def validatePin(self, pin):

        if self.pin is None:
            raise InvalidPinException(
                "PIN not set for this account"
            )

        if not self.verifyPin(pin):
            raise InvalidPinException(
                "Incorrect PIN"
            )

    def validateAmount(self, amount):

        if amount <= 0:
            raise InvalidAmountException(
                f"Amount must be positive. "
                f"Provided: ₹{amount}"
            )

    def setBalance(self, balance):

        self.balance = balance

    def updateDailyWithdrawalTotal(self, amount):

        pass

    # ===== Getters =====

    def getAccountNumber(self):
        return self.accountNumber

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getBalance(self):
        return self.balance

    def getStatus(self):
        return self.status