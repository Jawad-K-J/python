ch1=1
print("enter the limit of stack")
lim=int(input())
s=[]
t=[]
top=-1
while(ch1!=0):
        print ("_____Enter your choice_____")
        print ("1.push")
        print("2.pop")
        print( "3.display")
        ch=int(input())
        if ch==1:
                if top==lim-1:
                        print("stack is full")
                else:
                        top=top+1
                        print("enter the element u want to push")
                        ele=input()
                        t.append(ele)
                        s.extend(t)
                        t=[]
                        print("inserted successfully")
        elif ch==2:
                if top<0:
                        print("stack is empty")
                else:
                        s.pop()
                        top=top-1
                        print("deleted successfully")
        elif ch==3:
                if top<0:
                        print("stack is empty")
                else:
                        print (s)
        print("DO U WANT TO CONTINUE(0/1)")
        ch1=int(input())
