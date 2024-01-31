a=[]
n=int(input("Enter limit:"))
for x in range (0,n):
	element=input("Enter the word:")
	a.append(element)
max=0

temp=0
for i in a:
	if len(i)>max :
		max=len(i)
		temp=i
print("The largest word is:",temp)		
print("Length of the largest element:",max)

