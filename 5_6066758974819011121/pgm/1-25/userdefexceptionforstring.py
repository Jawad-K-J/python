class myerror(Exception):
   pass

t = input("Enter the letter to raise exception:")
str = input("Enter any string:")
try:
    for k in str:
        if k==t:
            raise myerror
except myerror:
    print("letter ",t," not allowed")
else:
    print("String Entered is Valid")
