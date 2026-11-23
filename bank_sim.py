
from decimal import Decimal, ROUND_HALF_UP


def _to_decimal(value: float | int | str | Decimal) -> Decimal:
    return Decimal(str(value))


def _round_currency(amount: Decimal) -> float:
    return float(amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def deposit(balance: float | int | str | Decimal,
            amount: float | int | str | Decimal) -> float:
    """Add amount to balance and return the updated balance."""
    balance = _to_decimal(balance)
    amount = _to_decimal(amount)

    if balance < 0:
        raise ValueError("Balance cannot be negative.")

    if amount <= 0:
        raise ValueError("Deposit amount must be greater than zero.")

    return _round_currency(balance + amount)


def withdraw(balance: float | int | str | Decimal,
             amount: float | int | str | Decimal) -> float:
    """Subtract amount from balance if sufficient funds exist."""
    balance = _to_decimal(balance)
    amount = _to_decimal(amount)

    if balance < 0:
        raise ValueError("Balance cannot be negative.")

    if amount <= 0:
        raise ValueError("Withdrawal amount must be greater than zero.")

    if amount > balance:
        raise ValueError("Insufficient funds.")

    return _round_currency(balance - amount)


if __name__ == "__main__":
    current_balance = 1000.00

    current_balance = deposit(current_balance, 250.00)
    current_balance = withdraw(current_balance, 150.00)

    print(f"Balance after Phase 1 transactions: {current_balance:.2f}")
