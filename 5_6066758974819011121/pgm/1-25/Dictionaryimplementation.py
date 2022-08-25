x = {}
def create():
   print("Dictionary Successfully Created")
def add():
   m = int(input("Enter limit:"))
   for i in range(0,m):
      a = input("Enter the key to insert:")
      b = input("Enter the value to insert:")
      x[a] = b
   print("Dictionary after insertion:",x)
def remove():
   u = input("enter the position of value to remove:")
   x.pop(u)
   print("Dictionary after deletion:",x)
def modify():
   w = input("Enter the key/position to modify:")
   y = input("Enter the value to modify:")
   x[w] = y
   print("Dictionary after modification:",x)
def exitt():
   print("exiting...")
   exit()
while True:
   print("-----DICTIONARY-----")
   print("\n1.create\n2.add item\n3.remove item\n4.modify item\n5.exit")
   n = int(input("\nEnter your choice:"))
   if(n == 1):
      create()
   if(n == 2):
      add()
   if(n == 3):
      remove() 
   if(n == 4):
      modify() 
   if(n == 5):
      exitt()
