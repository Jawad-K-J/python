def fact(n):
	factorial = 1
	if int(n) >= 1:
		for i in range (1,int(n)+1):
   			factorial = factorial * i
	print("Factorail of ",n , " is : ",factorial)

def factwith(num):
	n=int(num)
	if(n==1):
   	   return n
	elif(n<1):
	   return ("NA")
	else:
	   return(n*factwith(n-1))
	print(factwith(n))

num= input("Enter a number: ")
while(1):
	print("\t1.factorial without recurssion \n\t2.factorial with recurssion\n enter any key for exit.....!!!")
	ch=int(input("\n \t Enter you choice : "))
	if(ch==1):
		fact(num)
	elif(ch==2):
		factwith(num)
	else:
		exit()
