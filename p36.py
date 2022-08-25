ch1=1
print("enter the limit of stack : ")
lim=int(input())
s=[]
t=[]
top=-1
while(ch1!=0):
	print("_____IMPLEMENTATION OF STACK_____ ")
	print( "1.push\n2.pop\n3.display\n4.exit")
	print("Enter your choice :")
	ch=int(input())
	if ch==1:
		if top==lim-1:
			print("stack is full")
		else:
			top=top+1
			print("enter the element to push:  ")
			ele=int(input())
			t.append(ele)
			s.extend(t)
			t=[]
			print ("Inserted successfully")
	elif ch==2:
		if top<0:
			print("stack is empty")
		else:
			s.pop()
			top=top-1
			print ("deleted successfully")
	elif ch==3:
		if top<0:
			print ("stack is empty")
		else:
			print(s)
	elif ch==4:
		exit(0)
	else:
		print("Invalid Chocie")
