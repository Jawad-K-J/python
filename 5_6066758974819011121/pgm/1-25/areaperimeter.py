print("......Rectange......")
l = int(input("Enter the lenght:"))
b = int(input("Enter the bredth:"))

def Rarea(l,b):
   return(l*b)
def Rperimeter(l,b):
   return(2*(l+b))

print("Area :",Rarea(l,b),"\nPerimeter :",Rperimeter(l,b))

print("......Circle......")
r = int(input("Enter the Radius:"))

def Carea(r):
   return(3.14*r*r)
def Cperimeter(r):
   return(2*3.14*r)

print("Area :",Carea(r),"\nPerimeter :",Cperimeter(r))
