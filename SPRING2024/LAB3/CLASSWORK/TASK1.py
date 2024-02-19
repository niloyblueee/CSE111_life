#1,1
class BankAccount:
  def __init__(self,name,typeacc):
    self.user_name=name
    self.account_type=typeacc
    self.balance=1.0

account1 = BankAccount("Bilbo", "Savings")
print("=====================================")
print(f"User Name: {account1.user_name}")
print(f"Balance: {account1.balance}")
print(f"Account Type:", account1.account_type)
print("=====================================")
account2 = BankAccount("Frodo", "Business")
print(f"User Name: {account2.user_name}")
print(f"Balance: {account2.balance}")
print(f"Account Type: {account2.account_type}")
print("=====================================")

#1.2
account1.balance=15.75
account2.balance=700.5

print(f"acc1Balance: {account1.balance}")
print(f"acc2Balance: {account2.balance}")