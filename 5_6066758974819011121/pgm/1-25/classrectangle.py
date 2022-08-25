class Rectangle:

   def __init__(self):
      self.w = 0
      self.l = 0
   def setsize(self,width,length):
      self.w = width
      self.l = length
   def perimeter(self):
      return(2*(self.w+self.l))
   def area(self):
      return(self.w*self.l)
 

q = Rectangle()
width = int(input("enter the width"))
length = int(input("enter the length"))
q.setsize(width,length) 
print("Perimeter:",q.perimeter()) 
print("Area:",q.area())
