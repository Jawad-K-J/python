a=[]
n=int(input("Number of elements in array:"))
print("Enter array elements:")
for i in range(0,n):
        l=int(input())
        a.append(l)
print("Original array: ")
print(a)
print("Enter number of shifts needed:")
s=int(input())
for i in range(0, s):    
    last=a[len(a)-1];
    for j in range(len(a)-1, -1,-1):
        a[j]=a[j-1];
    a[0]=last;   
print("\nArray after right rotation: ")
for i in range(0,len(a)):
        print(a[i])
