"""
Name: SUCHITRA YADAWAD
Training ID: PYT_07/26_WD_PM_BATCH1
Module Title: Session 9 - Error Handling
"""

from contextlib import contextmanager


def task_1():
    # -------------------- Task 1 --------------------
    # Library Inventory Reader (File Reading)

    print("-" * 10 + " Task 1 " + "-" * 10)

    try:
        # Part A: Read the file line by line
        with open("books.txt", "r") as f:
            count = 0

            for line in f:
                year = int(line.strip().split(",")[-1])

                if year > 2015:
                    count += 1

            print("Books after 2015:", count)

        # Part B: Read the entire file at once
        with open("books.txt", "r") as f:
            data = f.read()

            years = [
                int(line.strip().split(",")[-1])
                for line in data.splitlines()
            ]

            print("Oldest book year:", min(years))

    except FileNotFoundError:
        print("Error: books.txt not found.")


def task_2():
    # -------------------- Task 2 --------------------
    # Sales Data Logger (File Writing and Appending)

    print("\n" + "-" * 10 + " Task 2 " + "-" * 10)

    sales = int(input())

    try:
        # Append today's sales amount
        with open("sales_log.txt", "a") as f:
            f.write(str(sales) + "\n")

        # Read the updated file
        with open("sales_log.txt", "r") as f:
            lines = f.readlines()

        print("Total entries:", len(lines))
        print("Latest entry:", lines[-1].strip())

    except FileNotFoundError:
        print("Error: sales_log.txt not found.")


def task_3():
    # -------------------- Task 3 --------------------
    # Merging Monthly Reports (Context Managers & Multi-file I/O)

    print("\n" + "-" * 10 + " Task 3 " + "-" * 10)

    try:
        with open("data1.txt", "r") as f1, \
             open("data2.txt", "r") as f2, \
             open("sum_data.txt", "w") as fout:

            for line1, line2 in zip(f1, f2):
                num1 = int(line1.strip())
                num2 = int(line2.strip())

                fout.write(str(num1 + num2) + "\n")

        # Read and print the contents of sum_data.txt
        with open("sum_data.txt", "r") as f:
            print(f.read(), end="")

    except (FileNotFoundError, ValueError) as e:
        print("Error:", e)


def task_4():
    # -------------------- Task 4 --------------------
    # Robust Transaction Processor (Exception Handling)

    print("\n" + "-" * 10 + " Task 4 " + "-" * 10)

    balance = 0

    try:
        with open("transactions.txt", "r") as f:
            for line_number, line in enumerate(f, start=1):
                action, amount = line.strip().split()

                try:
                    amount = int(amount)
                except ValueError:
                    print(f"Line {line_number}: invalid amount '{amount}'; skipping.")
                    continue

                if action == "deposit":
                    balance += amount
                elif action == "withdraw":
                    balance -= amount

        print("Final balance:", balance)

    except FileNotFoundError:
        print("Error: transactions.txt not found.")

    finally:
        print("Transaction processing completed.")


def task_5():
    # -------------------- Task 5 --------------------
    # Functional Context Manager for Safe File Operations

    print("\n" + "-" * 10 + " Task 5 " + "-" * 10)

    @contextmanager
    def safe_file_manager(filename, mode):
        try:
            file = open(filename, mode)
            yield file
        except FileNotFoundError:
            print("Error: file not found.")
        finally:
            if 'file' in locals() and not file.closed:
                file.close()
            print("File closed successfully.")

    try:
        with safe_file_manager("secure.txt", "w") as f:
            f.write("Confidential data")
    except FileNotFoundError:
        print("Error: secure.txt not found.")

task_2()