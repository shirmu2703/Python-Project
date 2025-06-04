
import random

# יצירת מאגר לקוחות כמילון
bank_customers = {}
bank_customers[1234] = {
    "id_number": "123456789",
    "first_name": "a",
    "last_name": "b",
    "birth_date": "27/03/2001",
    "email": "a@a.com",
    "balance": 0
}

def menu():
    print("""
    Please enter one of the options (1 to 8):
    1. Create account
    2. Deposit money
    3. Withdraw money
    4. Check Balance in account
    5. Close account
    6. Display all accounts holder list
    7. Total Balance in the Bank
    8. Quit
    """)
    choice = input("Enter your choice: ")
    return choice

def account_create(bank_customers):
    print("Creating a new account.")

    # first name
    while True:
        first_name = input("Enter first name: ").strip().capitalize()
        if not first_name.isalpha():
            print("Invalid first name. Please enter letters only.")
        else:
            break

    # last name
    while True:
        last_name = input("Enter last name: ").strip().capitalize()
        if not last_name.isalpha():
            print("Invalid last name. Please enter letters only.")
        else:
            break

    # ID number
    while True:
        id_number = input("Enter ID number (9 digits): ")
        if not id_number.isdigit() or len(id_number) != 9:
            print("Please enter a 9-digit numeric ID.")
            continue
        if any(str(cust["id_number"]) == id_number for cust in bank_customers.values()):
            print("ID already exists in the system.")
            continue
        break

    # birth date
    while True:
        birth_date = input("Enter birth date (DD/MM/YYYY): ")
        if len(birth_date) != 10 or birth_date[2] != "/" or birth_date[5] != "/":
            print("Please enter the date in the correct format (DD/MM/YYYY).")
            continue
        try:
            birth_year = int(birth_date[6:])
            if len(str(birth_year)) != 4:
                print("Year must be 4 digits.")
                continue
            if 2024 - birth_year < 16:
                print("Cannot open account for individuals under 16 years old.")
                continue
            break
        except ValueError:
            print("Invalid year. Please use numbers only.")
            continue

    # email
    while True:
        email = input("Enter email: ").lower()
        if "@" not in email or email.count("@") != 1 or not email.endswith(".com"):
            print("Invalid email format. Please enter a valid email ending with .com.")
        else:
            break

    # generate random account number
    import random
    account_number = random.randint(1000, 9999)
    while account_number in bank_customers:
        account_number = random.randint(1000, 9999)

    # save customer data
    bank_customers[account_number] = {
        "id_number": id_number,
        "first_name": first_name,
        "last_name": last_name,
        "birth_date": birth_date,
        "email": email,
        "balance": 0
    }

    print("Account created successfully.")
    print(f"Account number: {account_number}")
    print(f"Name: {first_name} {last_name}, ID: {id_number}, Birth Date: {birth_date}, Email: {email}")


def money_deposit(bank_customers):
    print("Depositing money into account.")
    while True:
        try:
            account_number = int(input("Enter account number: "))
            if account_number not in bank_customers:
                print("Account not found. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid account number. Please enter digits only.")

    while True:
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Deposit amount must be positive.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    bank_customers[account_number]["balance"] += amount
    print(f"Deposit of {amount} NIS into account {account_number} was successful.")
    print(f"New balance: {bank_customers[account_number]['balance']} NIS")


def money_withdraw(bank_customers):
    print("Withdrawing money from account.")
    while True:
        try:
            account_number = int(input("Enter account number: "))
            if account_number not in bank_customers:
                print("Account not found. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid account number. Please enter digits only.")

    if not user_authenticate(bank_customers, account_number):
        return

    while True:
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Withdrawal amount must be positive.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    if bank_customers[account_number]["balance"] - amount < -1000:
        print("Cannot withdraw this amount, exceeds overdraft limit.")
    else:
        bank_customers[account_number]["balance"] -= amount
        print(f"Withdrawal of {amount} NIS from account {account_number} was successful.")
        print(f"New balance: {bank_customers[account_number]['balance']} NIS")


def balance_check(bank_customers):
    print("Checking balance in account.")
    account_number = int(input("Enter account number: "))
    if account_number not in bank_customers:
        print("Account not found.")
        return
    print(f"Account number: {account_number}")
    print(f"Name: {bank_customers[account_number]['first_name']} {bank_customers[account_number]['last_name']}")
    print(f"Balance: {bank_customers[account_number]['balance']} NIS")

def account_close(bank_customers):
    print("Closing account.")
    account_number = int(input("Enter account number: "))
    if account_number not in bank_customers:
        print("Account not found.")
        return
    if not user_authenticate(bank_customers, account_number):
        return
    del bank_customers[account_number]
    print("Account closed successfully.")

def accounts_all_display(bank_customers):
    print("Displaying all accounts and balances.")
    for account_number, details in bank_customers.items():
        print(f"Account number: {account_number}")
        print(f"Name: {details['first_name']} {details['last_name']}")
        print(f"Balance: {details['balance']} NIS")

def balance_bank_total(bank_customers):
    total_balance = sum(details['balance'] for details in bank_customers.values())
    print(f"Total balance in the bank: {total_balance} NIS")

def user_authenticate(bank_customers, account_number):
    while True:
        birth_date = input("Please enter your birth date (DD/MM/YYYY): ")
        if len(birth_date) != 10 or birth_date[2] != "/" or birth_date[5] != "/":
            print("Invalid format. Please use DD/MM/YYYY.")
            continue
        if birth_date != bank_customers[account_number]["birth_date"]:
            print("Birth date does not match our records.")
            continue
        return True

def main():
    while True:
        choice = menu()
        if choice == '1':
            account_create(bank_customers)
        elif choice == '2':
            money_deposit(bank_customers)
        elif choice == '3':
            money_withdraw(bank_customers)
        elif choice == '4':
            balance_check(bank_customers)
        elif choice == '5':
            account_close(bank_customers)
        elif choice == '6':
            accounts_all_display(bank_customers)
        elif choice == '7':
            balance_bank_total(bank_customers)
        elif choice == '8':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
