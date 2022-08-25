def remove_char(s, i):
    a = s[ : i]
    b = s[i + 1: ]
    return a+b
def split_string(string):
    list_string = string.split(' ')
    return list_string

def join_string(list_string):
    string = '-'.join(list_string)
    return string

n=input("Enter your string: ")
m=input("Enter your word for remove character: ")
r=int(input("Enter i-th location to remove char "))
print("your string is :",n)

print("even length words:")
s=n.split(" ")
for i in s:
  if len(i)%2==0:
    print(i)
 
print("your word is :",m)
print("word after removing",r,"-th char is ")
print(remove_char(m,r-1))


list_string = split_string(n)
print("After Splitting: ",list_string)
res_string = join_string(list_string)
print("After joining: ",res_string)
