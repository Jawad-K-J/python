class rectangle():
   def __init__(self,width,length):
      self.width=width
      self.length=length
   def area(self):
      return self.width*self.length
   def perimeter(self):
      return 2*(self.width+self.length)
a=int(input("Enter length of rectangle : "))
b=int(input("Enter width of rectangle : "))
obj=rectangle(a,b)
print("Area of rectangle : ",obj.area())
print("Perimeter of rectangle : ",obj.perimeter())
print()
