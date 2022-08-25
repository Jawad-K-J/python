def recur_factorial(num):
   if num == 1:
       return num
   else:
       return num*recur_factorial(num-1)

n=int(input("Enter number:"))
num=n
fact=1
while(n>0):
    fact=fact*n
    n=n-1
print("Factorial of the number without recursion is: ",fact)

print("Factorial of the number with recursion is:", recur_factorial(num))
