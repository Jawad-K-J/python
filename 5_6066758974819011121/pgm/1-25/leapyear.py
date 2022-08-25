n = int(input("Enter the year::"))
a = n
f = 0
if(n % 400 == 0):
   f = 1	
if((n % 4 == 0)&(n % 100 != 0)):
   f = 1
if(f):
   print(a," is leap year")
else:
   print(a," is not a leap year")
