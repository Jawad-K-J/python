u=int(input("please enter the number of units you consumed in a month:"))
if(u<=100):
    Amount=u*1.5
    charge=25.00
elif(u<=200):
    Amount=(100*1.5)+(u-100)*2.5
    charge=50.00
elif(u<=300):
    Amount=(100*1.5)+(200-100)*2.5+(u-200)*4
    charge=75.00
elif(u<=350):
    Amount=(100*1.5)+(200-100)*2.5+(300-200)*4+(u-300)*5
    charge=100.00
else:
    Amount=0
    charge=1500.00
print("\nElecticity bill:",Amount+charge)
