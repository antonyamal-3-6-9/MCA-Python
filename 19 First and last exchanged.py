string=input("Enter a string:")
first=string[0]
last=string[-1]
newstring=last+string[1:-1]+first
print("After exchange :",newstring)
