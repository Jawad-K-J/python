n=int(input("enter the limit of numbers")) 
s=0 
for i in range(n):
	number=float(input("enter the numbers"))
	s+=number
	avg=s/n 
print("sum of numbers",s) 
print("avg of numbers",avg) 
