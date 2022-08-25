n = int(input("Enter your number:"))
def prime(n):
   if n > 1:
      f = 0
      for i in range(2, n):
         if (n % i) == 0:
            f = 1 
   if f == 0:
      print(n," is prime")
   else:
      print(n," is not a prime")
def armstrong(n):
   a = n
   s = 0
   while(n!=0):
      d=int(n%10)
      s=s+(d*d*d)
      n=n/10
   if a == s:
      print(a," is armstrong")
   else:
      print(a," is not armstrong")
def perfect(n):
   s = 0
   for i in range(1,n):
      if (n % i) == 0:
         s = s + i
   if s == n:
      print(n,"is perfect number")
   else:
      print(n," is not a perfect number")
def fibonocci(n):
   a = 0
   b = 1
   if (n == 0) or (n==1):
      print(n,"is fibonocci number")
   else:
      c = a + b
      if c == n:
         printf(n,"is a fibonocci number")
      else:
         print(n," is not a fibonocci number")
print("1.prime\n2.armstrong\n3.perfect number\n4.fibonocci")
m=int(input("Enter your choice:"))
if(m == 1):
   prime(n)
if(m == 2):
   armstrong(n)
if(m == 3):
   perfect(n)
if(m == 4):
   fibonocci(n)      
