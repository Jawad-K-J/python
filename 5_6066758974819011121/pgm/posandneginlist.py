list = []
n=int(input("How many elements do you want to insert : "))
for i in range(0,n,1):
	num=int(input("enter the element : "))
	list.append(num)
neg =[]
pos=[]
n=len(list)
for i in list:
	if(i>=0):
		pos.append(i)
	else:
		neg.append(i)
print("positive numbers in list are : ",pos)
print("negative numbers in list are : ",neg)
