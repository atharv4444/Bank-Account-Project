from gdb.exceptions.account_exception import AccountException


class InvalidAmountException(AccountException):
    """
    Thrown when an invalid amount is provided.
    """

    def __init__(self, message):
        super().__init__(message)