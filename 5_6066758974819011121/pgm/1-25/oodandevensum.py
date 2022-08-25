n = int(input("Enter the Number::"))
a = n
e = 0
o = 0
while(n > 0):
   d = int(n % 10)
   if(int(d % 2) == 0):
      e = e + d
   else:
      o = o + d 
   n = int(n / 10)
print("Even sum of ",a," is ",e)
print("Odd sum of ",a," is ",o)
