class Employee:
   count=0
   def __init__(self, name, desig, salary):
      self.name=name
      self.desig=desig
      self.salary=salary
      Employee.count+=1
   def displayCount(self):
      print("Total number of employees = %d " % Employee.count)
      print()

   def displayDetails(self):

      print( self.name, "\t", self.desig, "\t", self.salary)
e1=Employee("John", "Manager", 80000)
e2=Employee("Mike", "Team Leader", 50000)
e3=Employee("Derek", "Programmer", 30000)
e4=Employee("Raj", "Assistant", 25000)
e4.displayCount()
print("...Details of all employees...")
print("Name\tDesignation\tSalary")
e1.displayDetails()
e2.displayDetails()
e3.displayDetails()
e4.displayDetails()

