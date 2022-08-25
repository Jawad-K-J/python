import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="PYTHON")
cursor=db.cursor()
cursor.execute("create table student(rollno int primary key,name varchar(20),m1 int,m2 int,m3 int,tot int)")
n=int(input("enter the number of students: "))
for i in range(0,n):
	rollno=int(input("enter the roll number: "))
	name=input("enter the name: ")
	m1=int(input("enter mark 1: "))
	m2=int(input("enter mark 2: "))
	m3=int(input("enter mark 3: "))
	cursor.execute("Insert into student(rollno,name,m1,m2,m3) values('%d','%s','%d','%d','%d')"%(rollno,name,m1,m2,m3))
print ("Table Created Successfully")
sql="select * from student"
cursor.execute(sql)
result=cursor.fetchall()
for row in result:
	r=row[0]
	m1=row[2]
	m2=row[3]
	m3=row[4]
	t=m1+m2+m3
	cursor.execute("update student set tot='%d' where rollno='%d'"%(t,r))
cursor.execute("select * from student")
result=cursor.fetchall()
print ("Rollno\tName\tMark1\tMark2\tMark3\tTotal")
for row in result:
	r=row[0]
	n=row[1]
	m1=row[2]
	m2=row[3]
	m3=row[4]
	t=row[5]
	print ("%d\t%s\t%d\t%d\t%d\t%d" %(r,n,m1,m2,m3,t))
db.commit()
db.close()
