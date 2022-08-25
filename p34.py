from math import sqrt
print ("solve a quadratic equation a*x**2 + b*x + c = 0.")
try:
 a = float(input("a = "))
 b = float(input("b = "))
 c = float(input("c = "))
 discriminant = b**2 - 4*a*c
 root_of_discriminant = sqrt(discriminant)
 roots = ( (-b - root_of_discriminant)/(2*a), (-b + root_of_discriminant)/(2
*a))
 print("The roots are %g and %g" % roots)
except Exception as error:
 print("ERROR !!The exception message is: ", error)
