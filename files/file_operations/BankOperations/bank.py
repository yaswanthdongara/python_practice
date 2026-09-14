from menu import BankMenu
from operations import check_balance, deposit, create_account, accounts_data, withdraw
while True:
    BankMenu()
    try:
        ch = int(input("Enter your choice (0 to exit): "))
        if ch == 0:
            break
        elif ch == 1:
            check_balance()
        elif ch == 2:
            deposit()
        elif ch == 3:
            create_account();
        elif ch == 4:
            withdraw()
        elif ch == 5:
            accounts_data()
        else:
            print("Invalid choice. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")