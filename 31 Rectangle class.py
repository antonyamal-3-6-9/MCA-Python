class Rect:
	def __init__(self,breadth,length):
		self.breadth=breadth
		self.length=length
	def area(self):
		return self.breadth*self.length
	def perimeter(self):
		return (2*(self.breadth+ self.length))
length=int(input("Enter the length:"))
breadth=int(input("Enter the breadth:"))
obj=Rect(breadth,length)
print("Area:",obj.area())
print("Perimeter",obj.perimeter())
