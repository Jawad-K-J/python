def even():
	n=input(" Enter a string : ")
	s=n.split(" ")
	print("the even legnth words are :")
	for m in s:
		if len(m)%2==0:
			print(m)
def remove():
	string=input(" Enter a string : ")
	n=int(input(" Enter position to remove : "))
	a=string[ :n]
	b=string[n+1: ]
	c=a+b
	print("after removing ",n,"th position character the string is : ")
	print(c)
def split():
	n=input(" Enter a string : ")
	s=n.split(" ")
	print("after the split the string is  : ",s)
	print("after joining the string is : "," ".join(s))
	#print(m)
while(1):
	print("\n 1.to print even length words in a string \n 2.removing I-th character from a string \n 3. to split string and join string \n 5. exit")
	i=int(input("\t select a option : "))
	if(i==1):
		even()
	elif(i==2):
		remove()
	elif(i==3):
		split()
	else:
		exit(0)
