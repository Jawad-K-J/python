lim=int(input("enter ur limit of queue"))
ch1=1
front=-1
rear=-1
t=[]
q=[]
while(ch1!=0):
	print("Enter your choice")
	ch=int(input("1.insert\n2.delete\n3.display"))
	if(ch==1):
		if (rear==lim-1):
			print("queue is full")
		else:
			rear=rear+1
			ele=int(input("enter the element u want to insert"))
			t.append(ele)
			q.extend(t)
			t=[]
			print ("inserted successfully")
	elif(ch==2):
		if front==rear:
			print ("queue is empty")
		else:
			del q[0]
			front=front+1
			print("deleted successfully")
	elif(ch==3):
		if(front==rear):
			print ("queue is emptys")
		else:
			print(q)
	ch1=int(input("Do u want to continue(0/1)"))
