class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     @property
#     def balance(self):
#         return self._balance

#     @balance.setter
#     def balance(self, amount):
#         if amount < 0:
#             print("Invalid Amount!")
#         else:
#             self._balance = amount

#     @balance.deleter
#     def balance(self):
#         print("Account Closed!")
#         self._balance = 0


# acc1 = BankAccount("Sahil", 10000)
# print(acc1.balance)
# acc1.balance = 5000
# print(acc1.balance)
# acc1.balance = -1000
# del acc1.balance
# print(acc1.balance)