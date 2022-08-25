def mean(x,l):
   b = 0
   for i in range(0,l):
      b = b + x[i] 
   mean = b/l
   print("Mean:",mean)
def median(x,l):
   if( n % 2 == 0):
      m = int(l / 2)
      p = int((l + 1)/2)
      median = (x[m]+x[p])/2
   else:
      m = (l+1) / 2
      median = x[m]
   print("median:",median)
def mode(x,l):
   m = max(set(x),key = x.count)
   print("Mode:",m)
def exitt():
   print("exiting...")
   exit()

x = []
l = int(input("Enter limit:"))
for i in range(0,l,1):
   m = int(input("Enter the number:"))
   x.append(m)
while True:
   print("\n1.Mean\n2.Median\n3.Mode\n4.exit")
   n = int(input("\nEnter your choice:"))
   if(n == 1):
      mean(x,l)
   if(n == 2):
      median(x,l)
   if(n == 3):
      mode(x,l) 
   if(n == 4):
      exitt()
