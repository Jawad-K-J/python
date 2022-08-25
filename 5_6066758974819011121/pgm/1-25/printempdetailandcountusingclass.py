class Employee:
   empcount = 0
   def __init__(self,name,desig,sal):
      self.name = name
      self.desig = desig
      self.sal = sal
      Employee.empcount += 1

i = 1
count = 0
e = []
while i>0:
   name = input("Enter name:")
   desig = input("Enter Designation:")
   sal = input("Enter salary:")
   e.append(Employee(name,desig,sal))
   i = int(input("Do you what to continue(1/0):"))
   count += 1
n = 0
print("......Employee Details......")
while n < count:
   print("\nName:",e[n].name,"\nDesignation:",e[n].desig,"\nSalary:",e[n].sal)
   n += 1
print("Total number of Employees :",Employee.empcount)
