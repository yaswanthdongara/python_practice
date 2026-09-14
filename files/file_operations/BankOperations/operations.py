import pickle
import random
def check_balance():
    try:
        account_number = int(input("Enter your account number: "))
        with open("files/file_operations/BankOperations/account.txt", "rb") as fp:
            try:
                records = pickle.load(fp)
                for record in records:
                    if record['account_number'] == account_number:
                        balance = record['balance']
                        print(f"Your current balance is: 💰 {balance}")
                        break
                else:
                    print("Account number not found.")
            except EOFError:
                print("No account records found. Please create an account first.")
                return
    except FileNotFoundError:
        print("Account file not found. Please create an account first.")
        return
def deposit():
    try:
        account_number = int(input("Enter your account number: "))
        amount = float(input("Enter the amount to deposit: "))
        with open("files/file_operations/BankOperations/account.txt", "rb") as fp:
            records = pickle.load(fp)
            for record in records:
                if record['account_number'] == account_number:
                    record['balance'] += amount
                    print(f"Successfully deposited 💰 {amount}. New balance: 💰 {record['balance']}")
                    break
            else:
                print("Account number not found.")
        with open("files/file_operations/BankOperations/account.txt", "wb") as fp:
            pickle.dump(records, fp)
    except FileNotFoundError:
        print("Account file not found. Please create an account first.")
    except EOFError:
        return
def create_account():
    name = input("Enter your name: ")
    balance = 0.0
    account_number = random.sample(range(10000, 100000), 1)[0]
    account_data = {
        'account_number': account_number,
        'name': name,
        'balance': balance
        }
    try:
        with open("files/file_operations/BankOperations/account.txt", "rb") as fp:
            records = pickle.load(fp)
            records.append(account_data)
    except (FileNotFoundError, EOFError):
        records = [account_data]
    with open("files/file_operations/BankOperations/account.txt", "wb") as fp:
        pickle.dump(records, fp)
    print(f"Account created successfully! Your account number is: {account_number}")
def accounts_data():
    try:
        with open("files/file_operations/BankOperations/account.txt", "rb") as fp:
            records = pickle.load(fp)
            for record in records:
                print(f"Account Number: {record['account_number']}, Name: {record['name']}, Balance: 💰 {record['balance']}")
    except EOFError:
        return
    except FileNotFoundError:
        print("Account file not found. Please create an account first.")
        return
def withdraw():
    try:
        account_number = int(input("Enter your account number: "))
        amount = float(input("Enter the amount to withdraw: "))
        with open("files/file_operations/BankOperations/account.txt", "rb") as fp:
            records = pickle.load(fp)
            for record in records:
                if record['account_number'] == account_number:
                    if record['balance'] >= amount:
                        record['balance'] -= amount
                        print(f"Successfully withdrew 💰 {amount}. New balance: 💰 {record['balance']}")
                    else:
                        print("Insufficient balance.")
                    break
            else:
                print("Account number not found.")
        with open("files/file_operations/BankOperations/account.txt", "wb") as fp:
            pickle.dump(records, fp)
    except FileNotFoundError:
        print("Account file not found. Please create an account first.")
    except EOFError:
        return