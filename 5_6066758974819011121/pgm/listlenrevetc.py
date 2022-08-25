def length(list):
	print("The length of list is: ", len(list))
def exist(list):
	flag=0
	n=int(input("Enter element to check"))
	flag=list.count(n)
	if(flag==0):
		print("Element Not Exists")
	else:
		print("Element Exists")
def rev(list):
	l=[]
	for i in list:
		l.insert(0,i)
	print(l)
def sorting(list):
	l=[]
	list.sort()
	print(list)
newList = []
n=int(input("How many elements do you want to insert : "))
for i in range(0,n,1):
	num=int(input("enter the element : "))
	newList.append(num)
while(1):
	print("\n1.To find the length of the string\n2.to find the reverse of the list\n3.element exist or not in a lis\n4.To list sorting\npress any to exit!!!!")
	i=int(input("*********************select a option*********************\n\t:"))
	if(i==1):
		length(newList)
	elif(i==2):
		rev(newList)
	elif(i==3):
		exist(newList)
	elif(i==4):
		sorting(newList)
	else:
		exit()
