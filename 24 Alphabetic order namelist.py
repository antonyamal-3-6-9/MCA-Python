a=[]
n=int(input("Enter no. of students:"))
for i in range(0,n):
	element=input("Enter name of student:")
	a.append(element)
a.sort()
print("The name of students in order:")
for x in a:
	print(x)
