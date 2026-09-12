from gdb.domain.account_factory import AccountFactory


def main():
    print("=== Activity 12: Factory-Driven System Suite ===")

    # Step 1: Create all accounts ONLY through AccountFactory
    savings = AccountFactory.create_account(
        "SAVINGS", "SA1201", "Alice", 25,
        10000.0, "Active", "1234"
    )

    current = AccountFactory.create_account(
        "CURRENT", "CA1202", "Bob", 35,
        50000.0, "Active", "5678"
    )

    salary = AccountFactory.create_account(
        "SALARY", "SAL1203", "Charlie", 30,
        30000.0, "Active", "1111"
    )

    fixed_deposit = AccountFactory.create_account(
        "FIXEDDEPOSIT", "FD1204", "David", 40,
        100000.0, "Active", "9999"
    )

    # Step 2: Use only IAccount members
    accounts = [
        (savings, "Savings", 10000.0),
        (current, "Current", 50000.0),
        (salary, "Salary", 30000.0),
        (fixed_deposit, "FixedDeposit", 100000.0),
    ]

    for account, expected_type, expected_balance in accounts:
        assert account.get_account_type() == expected_type
        assert account.balance == expected_balance

    # Exercise deposit()
    savings.deposit(500.0)
    assert savings.balance == 10500.0

    current.deposit(1000.0)
    assert current.balance == 51000.0

    salary.deposit(2000.0)
    assert salary.balance == 32000.0

    fixed_deposit.deposit(5000.0)
    assert fixed_deposit.balance == 105000.0

    # Exercise withdraw()
    savings.withdraw(500.0)
    assert savings.balance == 10000.0

    current.withdraw(1000.0)
    assert current.balance == 50000.0

    salary.withdraw(2000.0)
    assert salary.balance == 30000.0

    fixed_deposit.withdraw(5000.0)
    assert fixed_deposit.balance == 100000.0

    print("All Factory-created accounts passed interface-only operations!")


if __name__ == "__main__":
    main()