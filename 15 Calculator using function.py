def add():
	n1=int(input("Enter first number :"))
	n2=int(input("Enter second number :"))
	return n1+n2
def sub():
	n1=int(input("Enter first number :"))
	n2=int(input("Enter second number :"))
	return n1-n2
def mul():
	n1=int(input("Enter first number :"))
	n2=int(input("Enter second number :"))
	return n1*n2
def div():
	n1=int(input("Enter first number :"))
	n2=int(input("Enter second number :"))
	return n1/n2
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice=int(input("Enter your choice:"))
if choice == 1:
	print(add())      
elif choice == 2:
		print(sub())    
elif choice == 3:
		print(mul())             
elif choice == 4:
		print(div()) 
else:
        print("Invalid Input")
		
