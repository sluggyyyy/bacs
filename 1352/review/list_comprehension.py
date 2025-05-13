class SavingsAccount: 
    def __init__(self, name: str = 'Unknown customer name', balance: float = 0, account_number: str = 'Unknown account number'):
        self.name = name
        self.balance = balance
        self.account_number = account_number
        
    def __str__(self):
        return(f'Account number: {self.account_number}, Name: {self.name}, Balance: {self.balance}')

    def deposit(self, add):
        self.balance += add
        
    def withdraw(self, sub):
        self.balance -= sub
        
def main():
    # Create account for DB Cooper, inital balance $200K, account number 700133289
    account1 = SavingsAccount("DB Cooper", 200000, "700133289")
    account1.withdraw(5000)
    account2 = SavingsAccount()
    for i in range(5):
        account2.deposit(10000)
    print(account1)
    print(account2)

if __name__ == "__main__":
    main()