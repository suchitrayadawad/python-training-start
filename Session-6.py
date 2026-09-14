"""
Name: SUCHITRA YADAWAD
Training ID: PYT_07/26_WD_PM_BATCH1
Module Title: Session 6 - Loops & Iteration I & II
"""


# -------------------- Task 1 --------------------
print("-" * 10 + " Task 1 " + "-" * 10)

data = "Alpha_User 101! #Beta$ & Gamma_99"

cleaned_data = ""

for char in data:
    if char.isalpha():
        cleaned_data += char
    elif char == " ":
        cleaned_data += " "
        pass

print("Cleaned data:", cleaned_data)


# -------------------- Task 2 --------------------
print("\n" + "-" * 10 + " Task 2 " + "-" * 10)

prices = [120.5, 118.2, 122.0, 115.5, 125.0]

starting_price = prices[0]

for index in range(1, len(prices)):
    percentage_change = ((prices[index] - starting_price) / starting_price) * 100

    print(
        f"Index {index}: Price = {prices[index]}, "
        f"Change = {percentage_change:.2f}%"
    )

    if percentage_change < -5:
        print("SELL ALERT - Index:", index)


# -------------------- Task 3 --------------------
print("\n" + "-" * 10 + " Task 3 " + "-" * 10)

service_status = {
    "Auth": "200 OK",
    "Cache": "500 Error",
    "Database": "200 OK",
    "Proxy": "404 Not Found"
}

for service, status in service_status.items():
    if "200" in status:
        print(service, "Service Healthy")
        continue

    print(service, "Service Critical")


# -------------------- Task 4 --------------------
print("\n" + "-" * 10 + " Task 4 " + "-" * 10)

import random

numbers = [random.randint(1, 50) for _ in range(20)]

print("List:", numbers)

target = int(input("Enter a number to search: "))

found = False
found_index = -1

for index, value in enumerate(numbers):
    print(f"Analyzing index [{index}]...")

    if value == target:
        found = True
        found_index = index
        break

if found:
    print(f"Target found at index {found_index}.")

    if found_index < len(numbers) - 1:
        print("Search was efficient because it stopped before the end.")
    else:
        print("Search was exhaustive because every element was checked.")
else:
    print("Target was not found.")
    print("Search was exhaustive because every element was checked.")


# -------------------- Task 5 --------------------
print("\n" + "-" * 10 + " Task 5 " + "-" * 10)

while True:
    command = input("Enter command (status, reset, exit): ").lower()

    match command:
        case "status":
            print("System status: Operational")

        case "reset":
            print("System has been reset.")

        case "exit":
            print("Exiting system...")
            break

        case _:
            print("Invalid command.")


# -------------------- Task 6 --------------------
print("\n" + "-" * 10 + " Task 6 " + "-" * 10)

for row in range(5):
    for col in range(5):
        if row == 2 and col == 2:
            continue

        print(f"({row}, {col})")


# -------------------- Task 7 --------------------
print("\n" + "-" * 10 + " Task 7 " + "-" * 10)

battery = 0

while battery <= 100:
    battery += 5

    if battery == 40 or battery == 60:
        print("Charging...")

    if battery == 80:
        pass  # Placeholder for Slow Charge Mode

    if battery == 100:
        print("Fully Charged")
        break


# -------------------- Task 8 --------------------
print("\n" + "-" * 10 + " Task 8 " + "-" * 10)

# I use a for loop to process each sensor reading one by one.
# continue skips invalid readings, while break stops processing when "ERROR" occurs.

logs = [22, 25, "TIMEOUT", 28, 0, "ERROR", 30]

total = 0
count = 0

for reading in logs:
    if reading == "TIMEOUT":
        continue

    if reading == 0:
        continue

    if reading == "ERROR":
        break

    total += reading
    count += 1

average = total / count

print("Average temperature:", average)


# -------------------- Task 9 --------------------
print("\n" + "-" * 10 + " Task 9 " + "-" * 10)

print("Prime numbers between 2 and 50:")

for number in range(2, 51):
    is_prime = True

    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break  # Stop checking once a factor is found

    if is_prime:
        print(number, end=" ")

# I use nested for loops to check each number for possible factors.
# break stops the inner loop as soon as a factor is found, making the search more efficient.


# -------------------- Task 10 --------------------
print("\n" + "-" * 10 + " Task 10 " + "-" * 10)

# I use a while loop because the user can make multiple purchases until the transaction ends.
# continue allows another choice for invalid or unaffordable items, while break ends the transaction.

balance = 50
items = {"Soda": 15, "Chips": 10, "Candy": 5}

while True:
    print("\nBalance:", balance)
    print("Items:", items)

    choice = input("Choose an item (Soda, Chips, Candy) or type 'finish': ").strip()

    if choice.lower() == "finish":
        print("Transaction finished.")
        break

    if choice not in items:
        print("Invalid item. Please choose again.")
        continue

    price = items[choice]

    if price > balance:
        print("Insufficient balance. Choose something else.")
        continue

    balance -= price
    print(choice, "purchased successfully.")
    print("Remaining balance:", balance)

    if balance == 0:
        print("Balance is 0. Transaction finished automatically.")
        break

    # Future refund functionality can be added here.
    pass
