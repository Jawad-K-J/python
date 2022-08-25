class Full(Exception):
	def __init__(self):
		print("Can't insert any element,stack overflow!!")

class Empty(Exception):
	def __init__(self):
		print("Can't delete any element,stack underflow!!")

class stack:
	def __init__(self):
		self.s = []
		self.top = -1
		self.n = int(input("Enter the size:"))
	def push(self,item):
		try:
			if self.top >= self.n-1:
				raise Full
		except Full:
    			print(message)
		else:
			self.top += 1
			self.s.append(item)
	def pop(self):
		try:
			if self.top <= -1:
				raise Empty
		except Full:
    			print(message)
		else:
			print(self.s[self.top]," is poped")
			self.top=self.top-1
			self.s.pop()
	def display(self):
		if self.top >= 0:
			print(self.s)
		else:
			print("Stack is empty")

S = stack()
i = 1
while i>0:
   print("......Stack operations......")
   print("1.Push\n2.Pop\n3.Display\n4.Exit")
   m = int(input("Enter your choice:"))
   if(m == 1):
      item = input("Enter the item to push:")
      S.push(item)
   if(m == 2):
      S.pop()
   if(m == 3):
      S.display()
   if(m == 4):
      i = 0

