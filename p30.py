
list1 = []
n = int(input("Enter number of elements : "))
print("Enter the elements:")
for i in range(0, n):
            ele = int(input())
            list1.append(ele)
product = 1
s = 0
print("List is:",list1)
for i in list1:
    product = product * i
    s = s + i
print("Sum  of elements: ",s)          
print("Product of elements: ",product) 

