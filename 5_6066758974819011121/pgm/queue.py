q=[]
def Enqueue():
        n=int(input("\nEnter the size of Queue : "))
        for i in range(0,n):
                if len(q)==n: 
                        print("Queue is Full...")
                else:
                        element=input("Enter the element : ")
                        q.append(element)
def dequeue():
        if not q:
                print("Queue is Empty...")
        else:
                e=q.pop(0)
                print("\nelement removed...",e)
def display():
        print(q)
while True:
        print("\nQUEUE IMPLEMENTATION\n1.Add \n2.Delete \n3.Display \n4.Quit")
        print("\nEnter the choice : ")
        choice=int(input())
        if choice==1:
                Enqueue()
        elif choice==2:
                dequeue()
        elif choice==3:
                display()
        elif choice==4:
                break
        else:
                print("Invalid Option...")
