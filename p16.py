class myclass:
	count =0
	def __init__(self):
		self.x=1
		myclass.count +=1
		print("value of x [Instance variable] : ",self.x)
	def countprint(self):
		print("count [class variable] : ",myclass.count)
		
x1=myclass()
x1.countprint()
x2=myclass()
x2.countprint()
x3=myclass()
x3.countprint()

