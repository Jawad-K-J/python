l=[]
n=int(input("enter the limit:"))
print("enter the element:")
for i in range(0,n):
    l.append(int(input()))
ro=int(input("enter the no of times you want to rotate:"))
for j in range(0,ro):
    temp=l[0]
    for i in range(0,n-1):
            l[i]=l[i+1]
    l[n-1]=temp
print(l)
