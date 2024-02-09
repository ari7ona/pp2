class Account():
    def __init__(self, owner: str, balance: int):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount: int):
        self.balance += amount
    def withdraw(self, amount: int):
        if self.balance < amount:
            print('You have insufficient amount of money')
        else: self.balance -= amount
    def details(self):
        print ('Account', self.owner, 'balance is', self.balance, 'KZT')

client = Account('Akhan', 100)

client.details()

client.deposit(1900)
client.details()

client.withdraw(1000)
client.details()