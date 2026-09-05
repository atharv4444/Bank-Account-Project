from AccountExceptions import Account

from InvalidAmountException import InvalidAmountException
from InsufficientBalanceException import InsufficientBalanceException
from MinimumBalanceViolationException import (
    MinimumBalanceViolationException
)
from InactiveAccountException import InactiveAccountException
from InvalidPinException import InvalidPinException


# Display account information
def displayAccount(account):

    pinStatus = "Yes" if account.hasPin() else "No"

    print(
        f"Account #{account.getAccountNumber()} | "
        f"{account.getName()} ({account.getAge()} yrs) | "
        f"{account.getAccountType()} | "
        f"₹{account.getBalance()} | "
        f"{account.getStatus()} | "
        f"PIN: {pinStatus}"
    )


print("=" * 60)
print(" ACCOUNT TEST WITH EXCEPTIONS")
print("=" * 60)


# ============================================================
# Test 1: Valid Account Creation
# ============================================================

print(">>> Test 1: Valid Account Creation")

try:

    account1 = Account(
        1001,
        "John Doe",
        25,
        1000.0,
        "Savings"
    )

    print("SUCCESS:", end=" ")
    displayAccount(account1)

except Exception as error:
    print("EXCEPTION:", error)


# ============================================================
# Test 2: Invalid Age
# ============================================================

print(">>> Test 2: Invalid Age (under 18)")

try:

    account2 = Account(
        1002,
        "Young Kid",
        16,
        500.0,
        "Savings"
    )

except ValueError as error:
    print("EXCEPTION:", error)


# ============================================================
# Test 3: Invalid Account Type
# ============================================================

print(">>> Test 3: Invalid Account Type")

try:

    account3 = Account(
        1003,
        "Test User",
        25,
        500.0,
        "Invalid"
    )

except ValueError as error:
    print("EXCEPTION:", error)


# ============================================================
# Test 4: Minimum Balance on Creation
# ============================================================

print(">>> Test 4: Minimum Balance on Creation")
print("Creating Savings account with ₹300")

try:

    account4 = Account(
        1004,
        "Bob Wilson",
        25,
        300.0,
        "Savings"
    )

except ValueError as error:
    print("EXCEPTION:", error)


# ============================================================
# Test 5: Valid Deposit and Withdrawal
# ============================================================

print(">>> Test 5: Valid Deposit and Withdrawal")

try:

    account5 = Account(
        1005,
        "Alice Brown",
        30,
        1000.0,
        "Current"
    )

    print("Account:", end=" ")
    displayAccount(account5)

    account5.setPin(1234)
    print("Setting PIN 1234: SUCCESS")

    account5.deposit(500.0)
    print("Depositing ₹500.0: SUCCESS")
    print(f"Balance after deposit: ₹{account5.getBalance()}")

    account5.withdraw(200.0, 1234)
    print("Withdrawing ₹200.0: SUCCESS")
    print(f"Balance after withdrawal: ₹{account5.getBalance()}")

    displayAccount(account5)

except Exception as error:
    print("EXCEPTION:", error)


# ============================================================
# Test 6: Invalid Deposit
# ============================================================

print(">>> Test 6: Invalid Deposit (Negative Amount)")
print("Attempting to deposit ₹-100.0")

try:

    account5.deposit(-100.0)

    print("Depositing ₹-100.0: SUCCESS")

except InvalidAmountException as error:
    print("EXCEPTION:", error)


# ============================================================
# Test 7: Insufficient Balance
# ============================================================

print(">>> Test 7: Insufficient Balance")

try:

    account6 = Account(
        1006,
        "Charlie Green",
        35,
        500.0,
        "Savings"
    )

    account6.setPin(1234)

    print("Account:", end=" ")
    displayAccount(account6)

    print("Attempting to withdraw ₹1000.0")

    account6.withdraw(1000.0, 1234)

except InsufficientBalanceException as error:
    print("EXCEPTION:", error)


# ============================================================
# Test 8: Minimum Balance Violation
# ============================================================

print(">>> Test 8: Minimum Balance Violation")

try:

    account7 = Account(
        1007,
        "Diana Prince",
        28,
        1000.0,
        "Savings"
    )

    account7.setPin(1234)

    print("Account:", end=" ")
    displayAccount(account7)

    print("Attempting to withdraw ₹600.0")

    account7.withdraw(600.0, 1234)

except MinimumBalanceViolationException as error:
    print("EXCEPTION:", error)


# ============================================================
# Test 9: Inactive Account Operations
# ============================================================

print(">>> Test 9: Inactive Account Operations")

try:

    account8 = Account(
        1008,
        "Eve Wilson",
        32,
        2000.0,
        "Current"
    )

    print("Account:", end=" ")
    displayAccount(account8)

    account8.closeAccount()
    print("Closing account: SUCCESS")

    print(
        "Attempting to deposit ₹100.0 "
        "on closed account"
    )

    try:

        account8.deposit(100.0)

    except InactiveAccountException as error:
        print("EXCEPTION:", error)


    account8.reopenAccount()
    print("Reopening account: SUCCESS")

    account8.deposit(100.0)

    print("Depositing ₹100.0 after reopen: SUCCESS")
    print(
        f"Balance after deposit: "
        f"₹{account8.getBalance()}"
    )


except Exception as error:
    print("EXCEPTION:", error)


# ============================================================
# Test 10: PIN Verification
# ============================================================

print(">>> Test 10: PIN Verification")

try:

    account9 = Account(
        1009,
        "Frank Miller",
        40,
        1500.0,
        "Savings"
    )

    print("Account:", end=" ")
    displayAccount(account9)

    account9.setPin(1234)
    print("Setting PIN 1234: SUCCESS")

    account9.withdraw(200.0, 1234)

    print(
        "Withdrawing ₹200.0 "
        "with correct PIN: SUCCESS"
    )

    print(f"Balance: ₹{account9.getBalance()}")


    # Incorrect PIN

    print(
        "Attempting to withdraw ₹100.0 "
        "with incorrect PIN (9999)"
    )

    try:

        account9.withdraw(100.0, 9999)

    except InvalidPinException as error:
        print("EXCEPTION:", error)


    # PIN not set

    account10 = Account(
        1010,
        "No Pin User",
        25,
        1000.0,
        "Savings"
    )

    print(
        "Attempting to withdraw ₹100.0 "
        "without PIN set"
    )

    try:

        account10.withdraw(100.0, 1234)

    except InvalidPinException as error:
        print("EXCEPTION:", error)


except Exception as error:
    print("EXCEPTION:", error)


# ============================================================
# Test 11: All Accounts Summary
# ============================================================

print(">>> Test 11: All Accounts Summary")

displayAccount(account1)
displayAccount(account5)
displayAccount(account6)
displayAccount(account7)
displayAccount(account8)
displayAccount(account9)


print("=" * 60)
print(" TEST COMPLETED!")
print("=" * 60)