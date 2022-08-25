a=0
b=0
# opening a text file
file1 = open("File1.txt", "w")
file1.write("From the age of about twelve until he was seventeen Newton was educated at the  which taught Latin and Ancient Greek and probably imparted a significant foundation of mathematics. He was removed from school and returned to Woolsthorpe by Colsterworth by October  His mother, widowed for  second time, attempted to make him a farmer, an occupation he hated. Henry Stokes, master at the King's School, persuaded his mother  send him back to school. Motivated partly by a desire for revenge against a schoolyard bully, he became the top-ranked student distinguishing himself mainly by building and models of windmills.")
file1.close()
file1= open("File1.txt", "r")
for i in file1.readlines():
   l=i.split()
   a=l.count("to")
   b=l.count("the")
print("number of  'to' in file = ",a)
print("number of 'the' in file = ",b)
file1.close()
