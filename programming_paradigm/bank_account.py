class BankAccount():
    def __init__(self,account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance = self.account_balance + amount
        print(f"Deposited: ${amount}")

    def withdraw(self, amount):
       if amount <= self.account_balance:
          self.account_balance = self.account_balance - amount
          print(f"Withdrew: ${amount}")
       else:
          print(" Insufficient funds") 


    def display_balance(self):
      print(f"Current Balance: ${self.account_balance}")

ahmed = BankAccount(1500)

ahmed.deposit(2000)
ahmed.display_balance()