n = int(input("Enter Roll Number:"))
name = input("Enter Name:")
degree = input("Enter Degree:")
clg = input("Enter College:")
m = []
for i in range(0,3):
   mark = int(input("Enter mark:"))
   m.append(mark) 
student = (n,name,degree,clg,m)
print("-----student record-----\n")
print(student)
