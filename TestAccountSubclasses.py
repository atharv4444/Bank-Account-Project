from gdb.domain.savings_account import SavingsAccount
from gdb.domain.current_account import CurrentAccount


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
print(" ACCOUNT SUBCLASSES TEST (SAVINGS & CURRENT)")
print("=" * 60)


# ============================================================
# Test 1: Creating Accounts
# ============================================================

print(">>> Test 1: Creating Accounts")

savings = SavingsAccount(
    1001,
    "John Doe",
    25,
    1000.0
)

current = CurrentAccount(
    1002,
    "Jane Smith",
    30,
    2000.0
)

print("Savings Account:", end=" ")
displayAccount(savings)

print("Current Account:", end=" ")
displayAccount(current)


# ============================================================
# Test 2: Account Type and Minimum Balance
# ============================================================

print(">>> Test 2: Account Type and Minimum Balance")

print(
    f"Savings Account - Type: {savings.getAccountType()}, "
    f"Minimum Balance: ₹{savings.getMinimumBalance()}"
)

print(
    f"Current Account - Type: {current.getAccountType()}, "
    f"Minimum Balance: ₹{current.getMinimumBalance()}"
)


# ============================================================
# Test 3: Savings Interest
# ============================================================

print(">>> Test 3: Savings Account - Interest Calculation")

print("Savings Account:", end=" ")
displayAccount(savings)

print(
    f"Interest Rate: {savings.getInterestRate()}% per annum"
)

print(
    f"Interest for 1 year: "
    f"₹{savings.calculateInterest(1)}"
)

print(
    f"Interest for 2 years: "
    f"₹{savings.calculateInterest(2)}"
)

print(
    f"Interest for 5 years: "
    f"₹{savings.calculateInterest(5)}"
)

interest = savings.calculateInterest(2)

print(
    f"After 2 years with interest: "
    f"Balance would be ₹{savings.getBalance() + interest}"
)


# ============================================================
# Test 4: Current Account Overdraft
# ============================================================

print(">>> Test 4: Current Account - Overdraft Feature")

print("Current Account:", end=" ")
displayAccount(current)

print(
    f"Overdraft Limit: ₹{current.getOverdraftLimit()}"
)

print(
    f"Available Overdraft: "
    f"₹{current.getAvailableOverdraft()}"
)

print(
    f"Overdraft Used: "
    f"₹{current.getOverdraftUsed()}"
)

print(
    f"Is Using Overdraft: "
    f"{str(current.isUsingOverdraft()).lower()}"
)

print(
    "Withdrawing ₹1500.0 "
    "(goes below minimum balance of ₹1000)"
)

print(
    f"Balance before: ₹{current.getBalance()}"
)

try:

    current.withdraw(1500.0, 1234)

except Exception as error:

    print("EXCEPTION:", error)

else:

    print("Withdrawing: ₹1500.0 - SUCCESS")

    print(
        f"Balance after: ₹{current.getBalance()}"
    )

    print(
        f"Overdraft Used: "
        f"₹{current.getOverdraftUsed()}"
    )

    print(
        f"Available Overdraft: "
        f"₹{current.getAvailableOverdraft()}"
    )

    print(
        f"Is Using Overdraft: "
        f"{str(current.isUsingOverdraft()).lower()}"
    )


# Attempt excessive withdrawal

print(
    "Attempting to withdraw ₹4000.0 "
    "(would exceed overdraft)"
)

available = (
    current.getBalance()
    + current.getAvailableOverdraft()
)

print(
    f"Available funds: ₹{current.getBalance()} "
    f"(balance) + ₹{current.getAvailableOverdraft()} "
    f"(overdraft) = ₹{available}"
)

try:

    current.withdraw(4000.0, 1234)

except Exception as error:

    print("EXCEPTION:", error)


# Repay overdraft

print("Repaying overdraft of ₹500.0")

print(
    f"Balance before repayment: "
    f"₹{current.getBalance()}"
)

print(
    f"Overdraft Used before: "
    f"₹{current.getOverdraftUsed()}"
)

try:

    current.repayOverdraft(500.0)

    print("Repaying ₹500.0 - SUCCESS")

    print(
        f"Balance after repayment: "
        f"₹{current.getBalance()}"
    )

    print(
        f"Overdraft Used after: "
        f"₹{current.getOverdraftUsed()}"
    )

    print(
        f"Is Using Overdraft: "
        f"{str(current.isUsingOverdraft()).lower()}"
    )

except Exception as error:

    print("EXCEPTION:", error)


# ============================================================
# Test 5: Polymorphism
# ============================================================

print(">>> Test 5: Polymorphism - Treating Accounts Uniformly")

print("Processing accounts polymorphically:")

accounts = [
    savings,
    current,
    SavingsAccount(
        1003,
        "Bob Wilson",
        35,
        500.0
    ),
    CurrentAccount(
        1004,
        "Alice Brown",
        28,
        1500.0
    )
]

for account in accounts:

    print(
        f"Account #{account.getAccountNumber()} | "
        f"{account.getName()} ({account.getAge()} yrs) | "
        f"{account.getAccountType()} | "
        f"₹{account.getBalance()} | "
        f"{account.getStatus()} | "
        f"Type: {account.getAccountType()}, "
        f"Min Balance: ₹{account.getMinimumBalance()}"
    )

print(f"Total accounts: {len(accounts)}")

totalBalance = sum(
    account.getBalance()
    for account in accounts
)

print(
    f"Total balance across all accounts: "
    f"₹{totalBalance}"
)


# ============================================================
# Test 6: Validation
# ============================================================

print(">>> Test 6: Validation - Invalid Creation Attempts")

print(
    "Attempting to create SavingsAccount "
    "with ₹300 (below minimum)"
)

try:

    SavingsAccount(
        1005,
        "Invalid Savings",
        25,
        300.0
    )

except ValueError as error:

    print("EXCEPTION:", error)


print(
    "Attempting to create CurrentAccount "
    "with ₹500 (below minimum)"
)

try:

    CurrentAccount(
        1006,
        "Invalid Current",
        25,
        500.0
    )

except ValueError as error:

    print("EXCEPTION:", error)


print(
    "Attempting to create SavingsAccount "
    "with age 16"
)

try:

    SavingsAccount(
        1007,
        "Young User",
        16,
        500.0
    )

except ValueError as error:

    print("EXCEPTION:", error)


# ============================================================
# Test 7: Savings PIN and Operations
# ============================================================

print(">>> Test 7: Savings Account - PIN and Operations")

account5 = SavingsAccount(
    1008,
    "Charlie Green",
    40,
    2000.0
)

print("Savings Account:", end=" ")
displayAccount(account5)

account5.setPin(1234)

print("Setting PIN 1234: SUCCESS")

account5.deposit(500.0)

print("Depositing ₹500.0: SUCCESS")

print(
    f"Balance after deposit: "
    f"₹{account5.getBalance()}"
)

try:

    account5.withdraw(300.0, 1234)

    print(
        "Withdrawing ₹300.0 with correct PIN: SUCCESS"
    )

    print(
        f"Balance after withdrawal: "
        f"₹{account5.getBalance()}"
    )

except Exception as error:

    print("EXCEPTION:", error)


print(
    "Attempting to withdraw ₹2000.0 "
    "(would violate minimum balance)"
)

try:

    account5.withdraw(2000.0, 1234)

except Exception as error:

    print("EXCEPTION:", error)


# ============================================================
# Test 8: Current Account Status
# ============================================================

print(">>> Test 8: Current Account - Active Status Operations")

account6 = CurrentAccount(
    1009,
    "Diana Prince",
    35,
    3000.0
)

print("Current Account:", end=" ")
displayAccount(account6)

account6.closeAccount()

print("Closing account: SUCCESS")

print(
    "Attempting to deposit ₹100.0 "
    "on closed account"
)

try:

    account6.deposit(100.0)

except Exception as error:

    print("EXCEPTION:", error)


account6.reopenAccount()

print("Reopening account: SUCCESS")

account6.deposit(100.0)

print("Depositing ₹100.0 after reopen: SUCCESS")

print(
    f"Balance after deposit: "
    f"₹{account6.getBalance()}"
)


# ============================================================
# Test 9: All Accounts Summary
# ============================================================

print(">>> Test 9: All Accounts Summary")

displayAccount(savings)
displayAccount(current)
displayAccount(accounts[2])
displayAccount(accounts[3])
displayAccount(account5)
displayAccount(account6)


print("=" * 60)
print(" TEST COMPLETED!")
print("=" * 60)