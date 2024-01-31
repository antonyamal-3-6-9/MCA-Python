def change (string):
	char=string[0]
	newstring=char+string[1:].replace(char,'$')
	return newstring
a=input("Enter a string:")
print("The modified string :",change(a))

