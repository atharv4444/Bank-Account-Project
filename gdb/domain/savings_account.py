from AccountExceptions import Account


class SavingsAccount(Account):

    MINIMUM_BALANCE = 500.0
    ACCOUNT_TYPE = "Savings"
    INTEREST_RATE = 4.0

    def __init__(self, accountNumber, name, age, initialBalance):

        super().__init__(
            accountNumber,
            name,
            age,
            initialBalance
        )

    def getMinimumBalance(self):

        return self.MINIMUM_BALANCE

    def getAccountType(self):

        return self.ACCOUNT_TYPE

    def calculateInterest(self, years):

        if years < 0:
            raise ValueError(
                "Years must be non-negative"
            )

        return (
            self.getBalance()
            * (self.INTEREST_RATE / 100)
            * years
        )

    def getInterestRate(self):

        return self.INTEREST_RATE