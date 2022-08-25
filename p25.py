import MySQLdb

db=MySQLdb.connect("localhost","root","user@1234", "MyDB")

cursor=db.cursor() 
cursor.execute("Drop table student")

print("Existing Table Dropped")

cursor.execute("Create table student(rollno int,name varchar(10),m1 int,m2 int,m3 int,tot int)") 
n=int(input("Enter no. of students: "))
for i in range(0,n):
	rollno=int(input("Enter the rollno: ") )
	name=input("Enter the name: ")
	m1=int(input("Enter mark1: "))
	m2=int(input("Enter mark2: "))
	m3=int(input("Enter mark3: ")) 
	cursor.execute("Insert into student(rollno,name,m1,m2,m3)values('%d','%s','%d','%d','%d')"%(rollno,name,m1,m2,m3))
print("Table Created Successfully")
cursor.execute("Select * from student")
res=cursor.fetchall()
for row in res:
	r=row[0]
	m1=row[2]
	m2=row[3]
	m3-row[4]
	t=m1+m2+m3
	cursor.execute("Update student set tot='%d' where rollno='%d'"%(t,r))
cursor.execute("Select * from student")
res=cursor.fetchall()
print("Rollno\tName\tMark1\tMark2 \tMark3 Total")
for row in res:
	r=row[0]
	n=row[1]
	ml=row[2]
	m2=row[3]
	m3=row[4]
	t=row[5]
	print("%d\t%s\t%d\t%d\t%d\t%d"%(r,n,m1,m2,m3,t))
db.commit()
db.close()

