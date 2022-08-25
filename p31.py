def small_large(list1):
    list1.sort()
  
    print("Largest element is:", list1[-1])
    print("Smallest element is:", list1[0])
    print("Second Largest element is:", list1[-2])

 

li=[]
n=int(input("Enter size of list "))
print("Enter the elements:")
for i in range(0,n):
    e=int(input())
    li.append(e)
small_large(li)     


