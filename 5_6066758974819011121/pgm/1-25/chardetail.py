n = input("Enter the string::")
V = []
C = []
d = []
S = []
for i in n:
   if(i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'u' or i == 'U'):
      V.append(i)
   elif(i.isdecimal()):
      d.append(i)
   elif(('A'>=i<='Z')&('a'>=i<='z')):
      S.append(i)
   else:
      C.append(i)        
print("vowels in ",n," are:",V)
print("consonents in ",n," are:",C)
print("digits in ",n," are:",d)
print("special characters in ",n," are:",S)

