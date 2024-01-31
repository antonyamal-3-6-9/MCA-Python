D={}
n=int(input("Enter no. students:"))
for i in range (0,n):
	name=input("Enter student name:")
	per=int(input("Enter percentage:"))
	D[name]=per
l=list(D.items())
l.sort()
print(l)
