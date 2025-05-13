class SavingsAccount:
    def __init__(self, n: str="Unknown customer name", b: float=0, anum: str="Unknown account number"):
        self.name = n
        self.balance = b
        self.account_number = anum

    def __str__(self)->str:
        return f"Account number: {self.account_number}, Name: {self.name}, Balance: {self.balance:.2f}"

    def __repr__(self)->str:
        return self.__str__()     

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        self.balance -= amount


def main():
    # Create account for DB Cooper, inital balance $200K, account number 700133289
    account1 = SavingsAccount("DB Cooper", 200000, "700133289")
    account1.withdraw(5000)
    account2 = SavingsAccount()
    for i in range(5):
        account2.deposit(10000)
    print(account1)
    print(account2)

    account_list = []
    account_list.append(account1)
    account_list.append(account2)
    account_list.append(SavingsAccount("Faan Tone Liu", 47000000, "700133290"))
    # # output the contents of the new SavingsAccount:
    # print(account_list[2])
    for account in account_list:
        print(account)

    print(account_list)

if __name__ == "__main__":
    main()