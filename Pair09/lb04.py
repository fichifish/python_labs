class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        try: self.balance = float(balance)
        except: print("нононо містер фиш")
    def deposit(self, amount):
        if amount>0: self.balance+=amount
        else: print("Помилка поповнення")
    def withdraw(self, amount):
        if 0<amount<=self.balance: self.balance-=amount
        else: print(f"Помилка: недостатньо коштів для {amount}")
    def info(self):
        print(f"{self.owner}: баланс {self.balance}")

artem = Wallet("Artem", 65000)
fish = Wallet("Fish", 2000)
artem.deposit(6000)
artem.withdraw(4334)
artem.withdraw(100000)
fish.deposit(500)
fish.withdraw(2500)
artem.info()
fish.info()