def pow(b,e):
	if e==0:
		return 1
	elif e==1:
		return b
	else:
		return(b*pow(b,e-1))
base=int(input("Enter base:"))
exp=int(input("Enter exponential value: "))
print("Result:",pow(base,exp))
