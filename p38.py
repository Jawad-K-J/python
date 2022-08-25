A=[]
m=int(input("Enter M for M x N matrix : ")) 
n=int(input("Enter N for M x N matrix : ")) 
print("Enter the element ::>")
for i in range (m): 
    row=[]                                      
    for j in range(n):
        row.append(int(input()))          
    A.append(row) 
    row=[]
    
print("Display Array In Matrix Form")
for i in range(0,m):
    for j in range(0,n):
        print(A[i][j], end=" ")
    print() 
B=[]
p=int(input("Enter M for M x N matrix : ")) 
q=int(input("Enter N for M x N matrix : "))          
print("Enter the element ::>")
for i in range (p): 
    row=[]                                     
    for j in range(q):
        row.append(int(input()))           
    B.append(row) 
    row=[]
print("Display Array In Matrix Form")
for i in range(0,p):
    for j in range(0,q):
        print(B[i][j], end=" ")
    print() 
    
res=[]
for i in range (m):                                   
    for j in range(n):
        row.append(0)          
    res.append(row) 
    row=[]
if m==p and n==q:
	for i in range(m):
		for j in range(n): 
			res[i][j]= A[i][j] + B[i][j] 
else:
	print("row or column size exceeded")
print("The Resultant Matrix After Addition ::>")
for r in res:
    print(r)
res_sub=[]
for i in range (m):                                   
    for j in range(n):
        row.append(0)          
    res_sub.append(row) 
    row=[]
if m==p and n==q:
    for i in range(m):
        for j in range(n): 
            res_sub[i][j]= A[i][j] - B[i][j] 
    
else:
    print("row or column size exceeded")
print("The Resultant Matrix After substraction ::>")
for r in res_sub:
    print(r)
res_mul=[]
for i in range (m):                                   
    for j in range(q):
        row.append(0)          
    res_mul.append(row) 
    row=[]
if m==q:
    for i in range(len(A)): 
           for j in range(len(B[0])): 
                  for k in range(len(B)): 
                         res_mul[i][j] += A[i][k] * B[k][j] 
print("The Resultant Matrix After Multiplication ::>")
for r in res_mul: 
       print(r)
