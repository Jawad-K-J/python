list = []
n=int(input("How many elements do you want to insert : "))
for i in range(0,n,1):
	num=int(input("enter the element : "))
	list.append(num)

l=[]
list.sort()
n=len(list)
print("Smallest element in the list= ",list[0])
print("Second largest element in the list= ",list[n-2])
print("largest element in the list= ",list[n-1])
