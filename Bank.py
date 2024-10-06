class BankAccount:
    # Class variable for interest rate
    interest_rate = 0.05

    def __init__(self, account_holder):
        # Instance variables
        self.account_holder = account_holder
        self.balance = 0  # Initial balance set to zero

    def deposit(self, amount):
        #Adding the amount to the balance.
        if amount > 0:
            self.balance += amount
            print(f'{amount} has been deposited. Your New balance is: {self.balance}')
        else:
            print('Please Make a Deposit..!')

    def withdraw(self, amount):
        #Subtracts the amount from the balance if the funds are enough
        if amount <= self.balance:
            self.balance -= amount
            print(f'{amount} has been withdrawn. Your New balance is: {self.balance}')
        else:
            print('Insufficient funds')

    def apply_interest(self):
        #Adds interest to the current balance based on the class variable interest_rate
        interest = self.balance * BankAccount.interest_rate
        self.balance += interest
        print(f'Interest of {interest} has been applied. Your New balance is: {self.balance}')

    def display_account_info(self):
        #Displays the account holder’s name and the current balance.
        print(f'Account Holder: {self.account_holder}')
        print(f'Current Balance: {self.balance}')


#Accounts with different account holders.
account1 = BankAccount('Joshua')
account2 = BankAccount('Roland')

#Performing a deposits and a withdrawal for each account
account1.deposit(1000)
account1.withdraw(200)

account2.deposit(500)
account2.withdraw(100)

#Apply interest to each account
account1.apply_interest()
account2.apply_interest()

#Display account information for each account
print("\n--- Account Information ---")
account1.display_account_info()
print("\n")
account2.display_account_info()
