lst = []
n = int(input("Enter number of elements : "))
print("Enter the elements\n")
for i in range(0, n):
            ele = int(input())
            lst.append(ele) 
print("Even numbers :")
for num in lst:
    if num % 2 == 0:
        print(num, end=" ")   
print("\nOdd numbers")
for num in lst:
    if num % 2 != 0:
       print(num, end = " ")
print("\n")
