newList = []
m=1
n=int(input("How many elements do you want to insert : "))
for i in range(0,n,1):
	num=int(input("enter the element : "))
	newList.append(num)
s=sum(newList)
print("The Sum Of List = ",s)
for i in newList:
	m=m*i
print("The Multiply the all elements in list = ",m)
