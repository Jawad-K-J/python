NumList = []
Positive = []
Negative = []

Number = int(input("Please enter the Total Number of List Elements : "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

for j in range(Number):
    if(NumList[j] >= 0):
        Positive.append(NumList[j])
    else:
        Negative.append(NumList[j])
print("Element in  List is : ", NumList)
print("Element in Positive List is : ", Positive)
print("Element in Negative List is : ", Negative)
