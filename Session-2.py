# Name: Suchitra Yadawad
# Date: 09-08-2026
# Module 2: Core Fundamentals


# Task - 1: The "Identity vs. Equality" Investigation

# Memory Mapping
x = 256
y = 256

print("\n========== Task 1: IDENTITY VS. EQUALITY ==========")
print("Memory address of x:",id(x))
print("Memory address of y:",id(y))

# The cache Limit
a = 257
b = 257

print("Memory address of a:",id(a))
print("Memory address of b:",id(b))

# Boolean Identity
is_same_identity = a is b
is_same_value = a == b

print("a is b:",is_same_identity)
print("a == b:",is_same_value)

# NoneType Check
status = None

print("Type of status:",type(status))
print("Memory address of status:",id(status))

# Single f-string output
print(
    f"x id: {id(x)}, y id: {id(y)}, "
    f"a id: {id(a)}, b id: {id(b)}, "
    f"a is b: {is_same_identity}, "
    f"a == b: {is_same_value}, "
    f"status id: {id(status)}"
)

# ==========================================
# Task 2: Advanced I/O and Type Casting Pipeline
# ==========================================

hourly_rate = float(input("Enter hourly rate: "))
hours_worked = int(input("Enter hours worked: "))
tax_bracket = float(input("Enter tax bracket (e.g., 0.2 for 20%): "))

gross = hourly_rate * hours_worked
net = gross - (gross * tax_bracket)

print("\n--- Task 2: Salary Calculation ---")
print(f"Hourly Rate: {hourly_rate}")
print(f"Hours Worked: {hours_worked}")
print(f"Tax Bracket: {tax_bracket}")
print(f"Gross Pay: {gross}")
print(f"Net Pay: {net}")

print("\n--- Type Validation ---")
print(f"Type of hourly_rate: {type(hourly_rate)}")
print(f"Type of hours_worked: {type(hours_worked)}")
print(f"Type of tax_bracket: {type(tax_bracket)}")

# ==========================================
# Task 3: Precision Engineering with F-Strings
# ==========================================

print("\n" + "=" * 40)
print(f"{'OFFICIAL PAYSLIP':=^40}")
print("=" * 40)

print(f"{'Hourly Rate:':<25}${hourly_rate:>14.3f}")
print(f"{'Hours Worked:':<25}${hours_worked:>14.3f}")
print(f"{'Tax Bracket:':<25}${tax_bracket:>14.3f}")
print(f"{'Gross Pay:':<25}${gross:>14.3f}")
print(f"{'Net Pay:':<25}${net:>14.3f}")

print("=" * 40)

# ==========================================
# Task 4: Complex Expressions & Operator Precedence
# ==========================================

a = 10
b = 5
c = 2
d = 3
e = 2
f = 8
g = 3

result = (a + b * c) / (d ** e) - f or g

is_valid = result > 0 and result is not None

print("\n" + "=" * 40)
print("TASK 4: COMPLEX EXPRESSION")
print("=" * 40)
print(f"Result: {result}")
print(f"Is Valid: {is_valid}")
print("=" * 40)

# ==========================================
# Task 5: Bitwise Permissions & Flag Manipulation
# ==========================================

GUEST = 1
USER = 2
ADMIN = 4
SUPERUSER = 8

# Combine GUEST and USER
current_access = GUEST | USER

# Elevate ADMIN using Left Shift
new_secure_level = ADMIN << 1

# Check if USER permission exists
has_user = (current_access & USER)==USER

# Toggle/remove GUEST permission
updated_access = current_access ^ GUEST

print("\n" + "=" * 40)
print("TASK 5: BITWISE PERMISSIONS")
print("=" * 40)

print(f"GUEST: {GUEST} -> {bin(GUEST)}")
print(f"USER: {USER} -> {bin(USER)}")
print(f"ADMIN: {ADMIN} -> {bin(ADMIN)}")
print(f"SUPERUSER: {SUPERUSER} -> {bin(SUPERUSER)}")

print(f"\nCurrent Access: {current_access} -> {bin(current_access)}")
print(f"New Secure Level: {new_secure_level} -> {bin(new_secure_level)}")
print(f"USER Check: {has_user} -> {bin(has_user)}")
print(f"Updated Access: {updated_access} -> {bin(updated_access)}")

print("=" * 40)