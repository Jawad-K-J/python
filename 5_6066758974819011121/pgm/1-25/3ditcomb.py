n = int(input("Enter first number:"))
m = int(input("Enter second number:"))
o = int(input("Enter third number:"))
d = []
d.append(n)
d.append(m)
d.append(o)
for i in range(0,3):
   for j in range(0,3):
      for k in range(0,3):
         if(i != j or j !=k or k != i):
            print(d[i],d[j],d[k])
