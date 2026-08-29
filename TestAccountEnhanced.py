from AccountEnhanced import AccountEnhanced


def display_account(account):
    pin_status = "Yes" if account.hasPin() else "No"

    print(
        f"Account #{account.getAccountNumber()} | "
        f"{account.getName()} ({account.getAge()} yrs) | "
        f"{account.getAccountType()} | "
        f"₹{account.getBalance()} | "
        f"{account.getStatus()} | "
        f"PIN: {pin_status}"
    )

print("\n")
print("=" * 60)
print(" ENHANCED ACCOUNT TEST (BOOLEAN RETURNS)")
print("=" * 60)


# Test 1: Valid Account Creation

print("\n>>> Test 1: Valid Account Creation")

account1 = AccountEnhanced(
    1001,
    "John Doe",
    25,
    1000.0,
    "Savings"
)

display_account(account1)


# Test 2: Invalid Age

print("\n>>> Test 2: Invalid Age (under 18)")
print("Creating account with age 16")

account2 = AccountEnhanced(
    1002,
    "Young Kid",
    16,
    500.0,
    "Savings"
)

print(f"Age auto-corrected to: {account2.getAge()}")
display_account(account2)


# Test 3: Invalid Account Type

print("\n>>> Test 3: Invalid Account Type")
print('Creating account with type "Invalid"')

account3 = AccountEnhanced(
    1003,
    "Test User",
    25,
    500.0,
    "Invalid"
)

print(f"Account type defaulted to: {account3.getAccountType()}")
display_account(account3)


# Test 4: Minimum Balance on Creation

print("\n>>> Test 4: Minimum Balance Enforcement on Creation")
print("Creating Savings account with ₹300 (below minimum)")

account4 = AccountEnhanced(
    1004,
    "Bob Wilson",
    25,
    300.0,
    "Savings"
)

print(
    f"Balance auto-corrected to minimum: "
    f"₹{account4.getBalance()}"
)

display_account(account4)


# Test 5: Withdrawal with Minimum Balance

print("\n>>> Test 5: Withdrawal with Minimum Balance")

account5 = AccountEnhanced(
    1005,
    "Alice Brown",
    30,
    1000.0,
    "Current"
)

account5.setPin(1234)

print("Initial:", end=" ")
display_account(account5)


# Valid withdrawal
amount = 200.0

if account5.withdraw(amount, 1234):
    print(f"Withdrawing ₹{amount}: SUCCESS")
    print(f"New balance: ₹{account5.getBalance()}")
else:
    print(f"Withdrawing ₹{amount}: FAILED")


print("After withdrawal:", end=" ")
display_account(account5)


# Invalid withdrawal because of minimum balance
amount = 900.0

if account5.withdraw(amount, 1234):
    print(f"Withdrawing ₹{amount}: SUCCESS")
else:
    print(
        f"Withdrawing ₹{amount} (would leave "
        f"₹{account5.getBalance() - amount}): "
        f"FAILED (Minimum balance violation)"
    )

print(f"Current balance: ₹{account5.getBalance()}")


# Test 6: Account Status Management

print("\n>>> Test 6: Account Status Management")

account6 = AccountEnhanced(
    1006,
    "Charlie Green",
    35,
    2000.0,
    "Savings"
)

print("Initial:", end=" ")
display_account(account6)


# Close account
if account6.closeAccount():
    print("Closing account: SUCCESS")
else:
    print("Closing account: FAILED")


print("After close:", end=" ")
display_account(account6)


# Try depositing into closed account
amount = 500.0

if account6.deposit(amount):
    print(f"Depositing ₹{amount} to closed account: SUCCESS")
else:
    print(
        f"Depositing ₹{amount} to closed account: "
        f"FAILED (Account inactive)"
    )


# Reopen account
if account6.reopenAccount():
    print("Reopening account: SUCCESS")
else:
    print("Reopening account: FAILED")


print("After reopen:", end=" ")
display_account(account6)


# Test 7: PIN Protection

print("\n>>> Test 7: PIN Protection")

account7 = AccountEnhanced(
    1007,
    "Diana Prince",
    28,
    1500.0,
    "Savings"
)


# Set PIN
if account7.setPin(1234):
    print("Setting PIN 1234: SUCCESS")
else:
    print("Setting PIN 1234: FAILED")


# Correct PIN
amount = 200.0

if account7.withdraw(amount, 1234):
    print(
        f"Withdrawing ₹{amount} with correct PIN (1234): "
        f"SUCCESS"
    )
    print(f"New balance: ₹{account7.getBalance()}")
else:
    print(
        f"Withdrawing ₹{amount} with correct PIN (1234): "
        f"FAILED"
    )


# Incorrect PIN
amount = 100.0

if account7.withdraw(amount, 9999):
    print(
        f"Withdrawing ₹{amount} with incorrect PIN (9999): "
        f"SUCCESS"
    )
else:
    print(
        f"Withdrawing ₹{amount} with incorrect PIN (9999): "
        f"FAILED (Incorrect PIN)"
    )


# Account without PIN
account8 = AccountEnhanced(
    1008,
    "No Pin User",
    25,
    1000.0,
    "Savings"
)

amount = 100.0

if account8.withdraw(amount, 1234):
    print(
        f"Withdrawing ₹{amount} with PIN not set: SUCCESS"
    )
else:
    print(
        f"Withdrawing ₹{amount} with PIN not set: "
        f"FAILED (PIN not set)"
    )


# Test 8: All Accounts Summary

print("\n>>> Test 8: All Accounts Summary")

display_account(account1)
display_account(account2)
display_account(account3)
display_account(account4)
display_account(account5)
display_account(account6)
display_account(account7)

print("\n")
print("=" * 60)
print(" ENHANCED TEST COMPLETED!")
print("=" * 60)
print("\n")