a=0
while a==0:
	print("1:prime or not")
	print("2:fibnocci")
	print("3:armstrong")
	print("4:perfect number")
	print("5:exit")
	p=int(input("enter your option"))
	if(p==1):
		num=int(input("enter the number"))
		flag=False
		if num>1:
			for i in range(2,num):
				if(num%i)==0:
					flag=True
					break
			if flag:
				print(num,"is not a prime number")
			else:
				print(num,"is a prime number")
	if(p==2):
		nterms=int(input("how many numbers"))
		n1,n2=0,1
		count=0
		if nterms<=0:
			print("please enter a positive integer")
		elif nterms==1:
			print("fibonacci sequence upto",nterms,":")
			print(n1)
		else:
			print("fibinacci sequence")
			while count<nterms:
				print(n1)
				nth=n1+n2
				n1=n2
				n2=nth
				count+=1
	if(p==3):
		num=int(input("enter a number"))
		sum=0
		temp=num
		while temp>0:
			digit=temp%10
			sum +=digit**3
			temp//=10
			if num==sum:
				print(num,"is an armstrong numbetr")
			else:
				print(num,"is not an armstrong")
	if(p==4):
		n=int(input("enter a number"))
		sum1=0
		for i in range(1,n):
			if(n%i==0):
				sum1=sum1+i
		if(sum1==n):
			print("the number is a perfect number")
		else:
			print("the number is not a perfect number")
	if(p==5):
		a=1s
