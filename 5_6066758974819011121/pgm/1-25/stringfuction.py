def letters(n):
   s=n
   t=0
   sc=0
   l=[]
   s = s.split(' ')
   n=n.split()
   for word in s:
      if(word.startswith("t")):
         t=t+1
      if(word.endswith("s")):
         sc=sc+1
      if(len(word)==6):
         l.append(word)
   print("The no of words in the string is:",len(n))
   print("Number of words starts with letter ‘t’:",t)
   print("Number of words ends with letter ‘s’:",sc)
   print("6 letters words are appearing",l)


n=input("Enter the string:")
letters(n)
