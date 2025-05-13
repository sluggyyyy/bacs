class BankAccount:
    next_account_id = 528001
    number_of_accounts = 0

    def __init__(self, n: str, b: float):
        self.name = n
        self.balance = b
        self.account_number = BankAccount.next_account_id
        BankAccount.next_account_id+=1
        BankAccount.number_of_accounts += 1

    def __str__(self)->str:
        return f"Name: {self.name}, Account id: {self.account_number}, Balance: ${self.balance}"

    def withdraw(self, a: float)->bool:
        if self.balance>=a:
            self.balance -= a
            return True
        else:
            return False
        
    def deposit(self, a: float):
        self.balance += a
        
class CheckingAccount(BankAccount):
    def __init__(self, n, b, min_b = 100):
        super().__init__(n, b)
        self.minimum_balance = min_b
        
    def __str__(self)-> str:
        return f"{super().__str__()}, Minimum balance: ${self.minimum_balance}"
    
    def withdraw(self, a: float)->bool:
        if self.balance >= a + self.minimum_balance:
            self.balance -= a
            return True
        else:
            return False
        
class SavingsAccount(BankAccount):
    def __init__(self, n, b):
        super().__init__(n, b)

    def withdraw(self, a):
        return super().withdraw(a)
    
    def deposit(self, a):
        return super().deposit(a)

def main():
    a2 = CheckingAccount("Penny Lane", 650.78)
    if a2.withdraw(560):
        print(f"New balance is {a2.balance}")
    else:
        print("Cannot withdraw, insufficient funds")
    print(a2)
    # a1 = BankAccount("Jane Bucks", 1215.23)
    # print(a1)
    # a1.deposit(1000.00)
    # a1.withdraw(98.60)
    # if a1.withdraw(3000):
    #     print(f"New balance is {a1.balance}")
    # else:
    #     print("Cannot withdraw, insufficient funds")

    # a2 = CheckingAccount("Penny Lane", 650.78)

if __name__ == "__main__":
    main()