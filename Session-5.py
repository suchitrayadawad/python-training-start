"""
Name: SUCHITRA YADAWAD
Training ID: PYT_07/26_WD_PM_BATCH1
Module Title: Session 5 - Control Flow
"""


# -------------------- Task 1 --------------------
print("-" * 10 + " Task 1 " + "-" * 10)

val_1 = 0
val_2 = 0.0
val_3 = ""
val_4 = None
val_5 = "False"

if val_1:
    print(f"Variable [val_1] with value [{val_1}] is evaluated as [TRUE]")
else:
    print(f"Variable [val_1] with value [{val_1}] is evaluated as [FALSE]")

if val_2:
    print(f"Variable [val_2] with value [{val_2}] is evaluated as [TRUE]")
else:
    print(f"Variable [val_2] with value [{val_2}] is evaluated as [FALSE]")

if val_3:
    print(f"Variable [val_3] with value [{val_3}] is evaluated as [TRUE]")
else:
    print(f"Variable [val_3] with value [{val_3}] is evaluated as [FALSE]")

if val_4:
    print(f"Variable [val_4] with value [{val_4}] is evaluated as [TRUE]")
else:
    print(f"Variable [val_4] with value [{val_4}] is evaluated as [FALSE]")

if val_5:
    print(f"Variable [val_5] with value [{val_5}] is evaluated as [TRUE]")
else:
    print(f"Variable [val_5] with value [{val_5}] is evaluated as [FALSE]")

# Analysis:
# 0, 0.0, an empty string, and None are falsy values in Python.
# "False" is a non-empty string, so Python evaluates it as True.


# -------------------- Task 2 --------------------
print("\n" + "-" * 10 + " Task 2 " + "-" * 10)

annual_income = float(input("Enter your annual income: "))
residency_status = input("Enter your residency status (Resident/Non-Resident): ")

if annual_income <= 30000:
    tax_rate = 0

elif annual_income <= 80000:
    if residency_status.strip().lower() == "resident":
        tax_rate = 10
    else:
        tax_rate = 15

else:
    tax_rate = 25

tax_amount = annual_income * tax_rate / 100
remaining_balance = annual_income - tax_amount

print(f"\nAnnual Income: ₹{annual_income:.2f}")
print(f"Tax Rate: {tax_rate}%")
print(f"Tax Amount: ₹{tax_amount:.2f}")
print(f"Remaining Balance: ₹{remaining_balance:.2f}")


# -------------------- Task 3 --------------------
print("\n" + "-" * 10 + " Task 3 " + "-" * 10)

status_code = int(input("Enter the HTTP status code: "))

match status_code:
    case 200:
        print("Success: OK")
    case 400:
        print("Client Error: Bad Request")
    case 404:
        print("Client Error: Not Found")
    case 500:
        print("Server Error: Internal Server Error")
    case _:
        print("Unknown Status Code")


# -------------------- Task 4 --------------------
print("\n" + "-" * 10 + " Task 4 " + "-" * 10)

# Task 4: Structural Pattern Matching with Combined Patterns

file_ext = input("Enter the file extension: ").strip().lower()

match file_ext:
    case ".jpg" | ".jpeg" | ".png":
        print("File Type: Image")

    case ".pdf" | ".docx" | ".doc":
        print("File Type: Document")

    case ".mp4" | ".mkv":
        print("File Type: Video")

    case _:
        print("File Type: Unsupported")


# -------------------- Task 5 --------------------
print("\n" + "-" * 10 + " Task 5 " + "-" * 10)

is_admin = input("Is the user an admin? (True/False): ").strip().lower() == "true"
has_security_key = input("Does the user have a security key? (True/False): ").strip().lower() == "true"
system_offline = input("Is the system offline? (True/False): ").strip().lower() == "true"

if (is_admin and has_security_key) or system_offline:
    print("OVERRIDE ACCESS GRANTED")
else:
    print("OVERRIDE ACCESS DENIED")