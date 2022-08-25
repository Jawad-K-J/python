class counter:
   classtotal = 0
   def __init__(self):
      self.mytotal = 0
   def increment(self):
      counter.classtotal+=1
      self.mytotal+=1

a = counter()
b = counter()

a.increment()
b.increment()
b.increment()

print(a.mytotal)
print(a.__class__.classtotal)
print(b.mytotal)
print(b.__class__.classtotal)
