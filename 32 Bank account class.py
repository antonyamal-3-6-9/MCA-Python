class Bank_account:
	def __init__(self):
		self.balance=0
		print("Welcome")
	def deposite(self):
		amount=float(input("Enter the amount to be deposited:"))
		self.balance=self.balance+amount
		print("Amount deposited",self.balance)
	def withdraw(self):
		amount=float(input("Enter amount to be withdrawn:"))
		if (self.balance >= amount):
			self.balance=self.balance-amount
			print("You withdrew;",amount)
		else:
			print("Insufficent balance!")
	def display(self):
		print("Your current balance:",self.balance)
s=Bank_account()
s.deposite()
s.withdraw()
s.display()

