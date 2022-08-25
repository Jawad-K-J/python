n = input("Enter Name:")
g = input("Enter Degree:")
m = int(input("Enter Mark:"))
print("Student Details\n")
print("Name:",n,"\nDegree:",g,"\nMark:",m,"\nGrade:")
if((m >= 90) & (m <=100)):
   print("A+")
elif((m >= 80) & (m <=89)):
   print("A")
elif((m >= 70) & (m <=79)):
   print("B+")
elif((m >= 60) & (m <=69)):
   print("B+")
elif((m >= 50) & (m <=59)):
   print("B")
elif((m >= 40) & (m <=49)):
   print("C")
elif((m >= 30) & (m <=39)):
   print("D")
else:
   print("Failed")
