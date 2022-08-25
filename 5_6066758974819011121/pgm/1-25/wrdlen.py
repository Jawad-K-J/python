n=input("Enter a string : ")
print("The even length words are :")
s=n.split(" ")
for i in s:
	if(len(i)%2==0):
		print(i)

