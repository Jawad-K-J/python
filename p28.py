def interList(sl):
    n = len(sl)    
    temp = sl[0]
    sl[0] = sl[n - 1]
    sl[n - 1] = temp 
    return sl

def swapList(list, p1, p2):     
    list[p1], list[p2] = list[p2], list[p1]
    return list
 


      

lst = []

n = int(input("Enter number of elements : "))
print("Enter the elements\n")
for i in range(0, n):
            ele = int(input())
            lst.append(ele)
print("Enter 2 positions to swap")
p1=int(input())
p2=int(input())
print("list :",lst)
print("interchanged list: ",interList(lst))
print("swapped list: ",swapList(lst, p1-1, p2-1))
