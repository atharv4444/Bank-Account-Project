from AccountExceptions import Account
from InsufficientBalanceException import InsufficientBalanceException


class CurrentAccount(Account):

    MINIMUM_BALANCE = 1000.0
    ACCOUNT_TYPE = "Current"
    OVERDRAFT_LIMIT = 5000.0

    def __init__(self, accountNumber, name, age, initialBalance):

        super().__init__(
            accountNumber,
            name,
            age,
            initialBalance
        )

        self.overdraftUsed = 0.0

    def getMinimumBalance(self):

        return self.MINIMUM_BALANCE

    def getAccountType(self):

        return self.ACCOUNT_TYPE

    def withdraw(self, amount, pin):

        self.validateActive()
        self.validatePin(pin)
        self.validateAmount(amount)

        # Normal balance + remaining overdraft
        availableFunds = (
            self.getBalance()
            + self.getAvailableOverdraft()
        )

        if amount > availableFunds:

            raise InsufficientBalanceException(
                f"Insufficient funds. Available: ₹{availableFunds} "
                f"(including ₹{self.OVERDRAFT_LIMIT} overdraft), "
                f"Requested: ₹{amount}"
            )

        newBalance = self.getBalance() - amount

        # Use overdraft when balance falls below minimum
        if newBalance < self.getMinimumBalance():

            overdraftAmount = (
                self.getMinimumBalance() - newBalance
            )

            self.overdraftUsed += overdraftAmount

        self.setBalance(newBalance)

        self.updateDailyWithdrawalTotal(amount)

    # ===== Overdraft Methods =====

    def getOverdraftLimit(self):

        return self.OVERDRAFT_LIMIT

    def getOverdraftUsed(self):

        return self.overdraftUsed

    def getAvailableOverdraft(self):

        return (
            self.OVERDRAFT_LIMIT
            - self.overdraftUsed
        )

    def isUsingOverdraft(self):

        return self.overdraftUsed > 0

    def repayOverdraft(self, amount):

        if amount <= 0:
            raise ValueError(
                "Repayment amount must be positive"
            )

        if amount > self.overdraftUsed:
            raise ValueError(
                f"Amount exceeds overdraft used "
                f"(₹{self.overdraftUsed})"
            )

        self.overdraftUsed -= amount

        self.setBalance(
            self.getBalance() + amount
        )