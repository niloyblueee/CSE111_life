class Account:
    def __init__(self, account_number, balance):
      self.account_number = account_number
      self.balance = balance
      self.account_type = "General"
      self.maturity = 0

    def print_details(self):
      print("------ Account details ------")
      print(f"Account Type: {self.account_type}, Maturity: {self.maturity} years")
      print(f"Account Number: {self.account_number}, Balance: ${self.balance:.2f}")

    def deposit(self, amount):
      self.balance += amount
      print(f"Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}")

    def withdraw(self, amount):
      if self.balance >= amount:
          self.balance -= amount
          print(f"Withdrew ${amount:.2f}. New Balance: ${self.balance:.2f}")
      else:
          print("Insufficient funds.")

    def year_passed(self, year):
      self.maturity += year
      print(f"Maturity of the account: {self.maturity} years")


class SavingsAccount(Account):
  def __init__(self,type,number,bal,interest,minimum):
      super().__init__(number,bal)
      self.inter_rate=interest
      self.minimum=minimum
      self.account_type=type

  def print_details(self):
      super().print_details()
      #print("------ Account details ------")
      #print(f"Account Type: {self.account_type}, Maturity: {self.maturity} years")
      #print(f"Account Number: {self.account_number}, Balance: ${self.balance:.2f}")
      print(f'Interest Rate : {self.inter_rate}, Minimum Limit: ${self.minimum}')

  def apply_interest(self):
      self.balance+= self.balance*self.inter_rate
      print(f'Interest applied. New balance {self.balance}')

  def withdraw(self, amount):
      if (self.balance - amount) >= self.minimum  :
        #super().withdraw(amount)
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New Balance: ${self.balance:.2f}")
      else:
        print("Insufficient funds.")  


class FixedDepositAccount(Account):
  def __init__(self,type,num,bal,age):
    super().__init__(num,bal)
    self.age,self.type=age,type
  
  def deposit(self, amount):
     print('You can not deposit in a fixed deposit accoun')

  def withdraw(self, amount):
    if self.age<=self.maturity:
      return super().withdraw(amount)
    else:
      print('Can not withdraw, Account is not matured')

print("-----------1------------")
account = Account("A203", 2000)
account.print_details()
print("-----------2------------")
account.deposit(400)
account.withdraw(1500)
account.year_passed(2)
print("-----------3------------")
account.print_details()
print("-----------4------------")
savings_account = SavingsAccount("Savings","SA123", 1000, 0.05, 500)
savings_account.print_details()
print("-----------5------------")
savings_account.deposit(400)
print("-----------6------------")
savings_account.withdraw(1000)
print("-----------7------------")
savings_account.withdraw(800)
print("-----------8------------")
savings_account.apply_interest()
print("-----------9------------")
savings_account.print_details()
print("-----------10------------")
fixed_account1= FixedDepositAccount("Fixed Deposit","FDA321", 10000, 5)
fixed_account1.print_details()
print("-----------11------------")
fixed_account1.deposit(400)
print("-----------12------------")
fixed_account1.year_passed(6)
print("-----------13------------")
fixed_account1.withdraw(10000)
print("-----------14------------")
fixed_account1.print_details()
print("-----------15------------")
fixed_account2 = FixedDepositAccount("Fixed Deposit","FDA300", 50000, 7)
fixed_account2.print_details()
print("-----------16------------")
fixed_account2.withdraw(10000)
