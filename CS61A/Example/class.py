class Account:
    def __init__(self,account_holder):
        self.balance=0
        self.holder=account_holder
    def deposit(self,amount):
        self.balance+=amount
        return self.balance
    def withdraw(self,amount):
        if amount>self.balance:
            return 'Insufficient funds'
        self.balance = self.balance-amount
        return self.balance

spock_account=Account('Spock')
spock_account.deposit(100)
spock_account.withdraw(90)
p=spock_account.withdraw(90)
print(p)
