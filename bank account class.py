class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance

    # Deposit method
    def deposit(self, amount):
        self.balance += amount
        return amount

    # Withdraw method
    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount

    # Check balance method
    def check_balance(self):
        print("Current balance:", self.balance)

    # Customer details method
    def customer_details(self):
        print("\nCustomer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of Opening:", self.date_of_opening)
        print("Balance:", self.balance)



account_number = input("Enter account number: ")
customer_name = input("Enter customer name: ")
date_of_opening = input("Enter date of account opening: ")
balance = float(input("Enter initial balance: "))


account = BankAccount(account_number, customer_name, date_of_opening, balance)


deposit_amount = float(input("Enter amount to deposit: "))
print("Deposited:", account.deposit(deposit_amount))


withdraw_amount = float(input("Enter amount to withdraw: "))
print("Withdrawn:", account.withdraw(withdraw_amount))


account.check_balance()


account.customer_details()
