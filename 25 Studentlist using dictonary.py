student={}
n=int(input("Enther the no. of students:"))
for i in range (0,n):
	name=input("Enter the name of the student:")
	age=int(input("Enter the age of the student:"))
	grade=input("Enter the grade of the student:")
	student[name]=age,grade
print(student)
