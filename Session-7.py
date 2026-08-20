"""
Name: SUCHITRA YADAWAD
Training ID: PYT_07/26_WD_PM_BATCH1
Module Title: Session 7 - Modular Code I
"""


# -------------------- Task 1 --------------------
# The Secure Vault Gateway
print("-" * 10 + " Task 1 " + "-" * 10)

def access_vault(user_id, *, pincode, biometric_id=None):
    """Validate vault access using keyword-only credentials.

    Args:
        user_id: Unique identifier of the user.
        pincode: Security PIN for the vault.
        biometric_id: Optional biometric identifier.

    Returns:
        True if the supplied credentials are present and valid.
    """
    if not user_id or not pincode:
        return False

    if biometric_id is not None and not biometric_id:
        return False

    return True

# Test cases for Task -1 
print("\n--- Task 1 ---")
print(access_vault("USER001", pincode="1234"))
print(access_vault("USER002", pincode="5678", biometric_id="BIO01"))
print(access_vault("", pincode="1234"))


# -------------------- Task 2 --------------------
# The Bulk Transfer Processor
print("\n" + "-" * 10 + " Task 2 " + "-" * 10)

def execute_bulk_transfer(sender_account, *amounts):
    """Process multiple transfers from a starting balance.

    Args:
        sender_account: Name or identifier of the sender.
        *amounts: Variable number of transfer amounts.

    Returns:
        The remaining balance after all transfers.
    """
    balance = 10000.0

    for amount in amounts:
        balance -= amount
        print(
            f"Transfer from {sender_account}: "
            f"{amount:.2f} | Remaining balance: {balance:.2f}"
        )

    return balance

# Test cases for Task - 2
print("\n--- Task 2 ---")
print("Final balance:", execute_bulk_transfer("ACC001", 1000, 500))
print("Final balance:", execute_bulk_transfer("ACC002", 0))
print("Final balance:", execute_bulk_transfer("ACC003", 250, 750, 1000))


# -------------------- Task 3 --------------------
# Dynamic Fee Policy
print("\n" + "-" * 10 + " Task 3 " + "-" * 10)

def calculate_net_amount(base_amount, **kwargs):
    """Apply dynamically supplied tax and fee rates.

    Args:
        base_amount: Starting monetary amount.
        **kwargs: Tax or fee rates expressed as decimal values.

    Returns:
        The amount after applying all supplied rates.
    """
    amount = base_amount

    for rate in kwargs.values():
        amount -= amount * rate

    return amount

# Test cases for Task - 3
print("\n--- Task 3 ---")
print(calculate_net_amount(1000, vat=0.15))
print(calculate_net_amount(1000, vat=0.15, service_fee=0.05))
print(calculate_net_amount(0, vat=0.15))


# -------------------- Task 4 --------------------
# The Currency Arbitrage Scanner
print("\n" + "-" * 10 + " Task 4 " + "-" * 10)

def get_market_rates(ticker):
    """Return buy price, sell price, and spread for a ticker.

    Args:
        ticker: Currency or market ticker symbol.

    Returns:
        A tuple containing buy price, sell price, and spread.
    """
    rates = {
        "USD": (83.0, 83.5),
        "EUR": (90.0, 90.8),
        "GBP": (105.0, 106.0),
    }

    buy_price, sell_price = rates.get(ticker.upper(), (0.0, 0.0))
    spread = sell_price - buy_price

    return buy_price, sell_price, spread

# Test cases for Task - 4
print("\n--- Task 4 ---")
buy, sell, spread = get_market_rates("USD")
print(buy, sell, spread)
print(get_market_rates("EUR"))
print(get_market_rates("XYZ"))


# -------------------- Task 5 --------------------
# Account Validation Wrapper
print("\n" + "-" * 10 + " Task 5 " + "-" * 10)

def validate_account_status(account_id):
    """Return account status using a nested tuple.

    Args:
        account_id: Unique account identifier.

    Returns:
        A nested tuple containing status code, active status,
        and KYC completion status.
    """
    accounts = {
        "ACC001": ("200", (True, True)),
        "ACC002": ("200", (True, False)),
        "ACC003": ("403", (False, False)),
    }

    return accounts.get(account_id, ("404", (False, False)))

# Test cases for Task - 5
print("\n--- Task 5 ---")
status, (active, kyc) = validate_account_status("ACC001")
print(status, active, kyc)

status, (active, kyc_complete) = validate_account_status("ACC002")
print(status, active, kyc_complete)

status, (_, kyc_complete) = validate_account_status("ACC003")
print("KYC complete:", kyc_complete)


# -------------------- Task 6 --------------------
# The Auditor's Google-Style Docstring
print("\n" + "-" * 10 + " Task 6 " + "-" * 10)

def calculate_compound_interest(
    principal, rate, times_compounded, years
):
    """Calculate the final value of a compound-interest investment.

    Args:
        principal: Initial amount invested.
        rate: Annual interest rate as a decimal.
        times_compounded: Number of times interest is compounded per year.
        years: Number of years the money is invested.

    Returns:
        The final amount after compound interest.

    Raises:
        ValueError: If the interest rate is negative.
    """
    if rate < 0:
        raise ValueError("Interest rate cannot be negative.")

    if times_compounded <= 0 or years < 0:
        raise ValueError(
            "Compounding frequency must be positive and years "
            "cannot be negative."
        )

    return principal * (
        1 + rate / times_compounded
    ) ** (times_compounded * years)

# Test cases for Task - 6
print("\n--- Task 6 ---")
print(calculate_compound_interest(10000, 0.05, 12, 2))
print(calculate_compound_interest(5000, 0.10, 4, 1))

try:
    print(calculate_compound_interest(1000, -0.05, 12, 1))
except ValueError as error:
    print("Error:", error)


# -------------------- Task 7 --------------------
# NumPy-Style Scientific Schema
print("\n" + "-" * 10 + " Task 7 " + "-" * 10)

def calculate_risk_score(data_points, sensitivity):
    """
    Calculate a simple risk score from data points.

    Parameters
    ----------
    data_points : array-like of float
        Numerical risk measurements.
    sensitivity : float
        Multiplier used to adjust the risk score.

    Returns
    -------
    float
        The calculated risk score.
    """
    if not data_points:
        return 0.0

    average = sum(data_points) / len(data_points)
    return float(average * sensitivity)

# Test cases for Task - 7
print("\n--- Task 7 ---")
print(calculate_risk_score([10.0, 20.0, 30.0], 1.5))
print(calculate_risk_score([5.0], 2.0))
print(calculate_risk_score([], 1.5))


# -------------------- Task 8 --------------------
# The "Print vs. Return" Audit 
print("\n" + "-" * 10 + " Task 8 " + "-" * 10)

def show_result():
    """Print a result without returning it."""
    print("Transaction processed successfully.")

# Test cases for Task - 8
print("\n--- Task 8 ---")
result = show_result()
print("Returned value:", result)

result = show_result()
print("Returned value:", result)

result = show_result()
print("Returned value:", result)


# -------------------- Task 9 --------------------
# Functional Pipeline Design
print("\n" + "-" * 10 + " Task 9 " + "-" * 10)

def clean_input(item, amount):
    """Clean and package invoice data into a tuple.

    Args:
        item: Invoice item name.
        amount: Invoice amount.

    Returns:
        A tuple containing cleaned item and amount.
    """
    return item.strip(), float(amount)


def apply_discount(invoice_data, discount_rate):
    """Apply a discount to invoice data.

    Args:
        invoice_data: Tuple containing item and amount.
        discount_rate: Discount percentage as a decimal.

    Returns:
        A tuple containing item and discounted amount.
    """
    item, amount = invoice_data
    discounted_amount = amount * (1 - discount_rate)
    return item, discounted_amount


def format_currency(invoice_data):
    """Format invoice data as currency text.

    Args:
        invoice_data: Tuple containing item and amount.

    Returns:
        A formatted invoice string.
    """
    item, amount = invoice_data
    return f"{item}: ₹{amount:.2f}"


def process_invoice(item, amount, discount_rate):
    """Process an invoice through the complete function pipeline.

    Args:
        item: Invoice item name.
        amount: Original invoice amount.
        discount_rate: Discount percentage as a decimal.

    Returns:
        A formatted invoice string.
    """
    cleaned_data = clean_input(item, amount)
    discounted_data = apply_discount(cleaned_data, discount_rate)
    return format_currency(discounted_data)

# Test cases for Task - 9
print("\n--- Task 9 ---")
print(process_invoice("Laptop", 50000, 0.10))
print(process_invoice("  Keyboard  ", 2000, 0.20))
print(process_invoice("Mouse", 1000, 0.00))


# -------------------- Task 10 --------------------
# The Fail-Safe Dispatcher
print("\n" + "-" * 10 + " Task 10 " + "-" * 10)

def dispatch_payment(amount):
    """Return payment result using a success/error result pattern.

    Args:
        amount: Payment amount to dispatch.

    Returns:
        A tuple containing success status and an error message or None.
    """
    if amount <= 0:
        return False, "Payment amount must be greater than zero."

    return True, None

if __name__ == "__main__":
    # Test cases for Task - 10
    print("\n--- Task 10 ---")

    success, error = dispatch_payment(5000)
    print(success, error)

    success, error = dispatch_payment(0)
    print(success, error)

    success, error = dispatch_payment(-100)
    print(success, error)