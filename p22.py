class MyError(Exception):
   pass
s=input("Enter a string : ")
try:
   c=input("Enter a character : ")
   for i in s:
      if i==c:
         raise MyError
except MyError:
   print("Exception caught\nGiven character found")
else:
   print("No such character found")

