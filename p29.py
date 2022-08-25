li=[]
n=int(input("Enter size of list "))
for i in range(0,n):
    e=int(input("Enter element of list "))
    li.append(e)
print('List is :', li)
print ("Lenght of the list = ", len(li))

li.reverse()
print('Reversed List:', li)

li.sort()
print('Sorted List:', li)



a=int(input("Enter element to search ")) 

if a in li:
   print("Element exist")
else:
   print("Element not exist")  
