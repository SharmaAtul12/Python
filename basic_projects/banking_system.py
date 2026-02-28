# banking_system.py

class BankAccount:
    
    # Constructor to initialize account
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    # Deposit method
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount Deposited Successfully!")
        else:
            print("Invalid deposit amount.")

    # Withdraw method
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print("Withdrawal successful!")

    # Display balance
    def check_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: {self.balance}")


def main():
    print("===== SIMPLE BANKING SYSTEM =====")

    name = input("Enter account holder name: ")
    account = BankAccount(name)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            print("Thank you for using banking system!")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()