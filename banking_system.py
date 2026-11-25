
class BankAccount:

    # Constructor
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    # Deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully!")
        else:
            print("Invalid deposit amount!")

    # Withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")

    # Check balance
    def check_balance(self):
        print("Current Balance:", self.balance)

    # Display account details
    def display_details(self):
        print("\n----- ACCOUNT DETAILS -----")
        print("Name:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


# Creating an object
account = BankAccount("Hardik", 123456, 1000)

# Banking menu
while True:

    print("\n===== SIMPLE BANKING SYSTEM =====")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Account Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == "3":
        account.check_balance()

    elif choice == "4":
        account.display_details()

    elif choice == "5":
        print("Thank you for using our banking system!")
        break

    else:
        print("Invalid choice! Try again.")
