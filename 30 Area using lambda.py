print("Rectangle")
l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
area=lambda l,b:l*b
perimeter=lambda l,b:2*(l+b)
print("Area of the Rectangle:",area(l,b))
print("Perimeter of the rectangle:",perimeter(l,b))
