from gdb.exceptions.account_exception import AccountException


class InactiveAccountException(AccountException):
    """
    Thrown when an operation is attempted
    on an inactive account.
    """

    def __init__(self, message):
        super().__init__(message)