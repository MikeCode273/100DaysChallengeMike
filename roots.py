# A program to display the roots of a quadratic equation
#inputs of the coefficients of a quadratic equation
import math
a=input("Enter valua for a:")
b=input("Enter valua for b:")
c=input("Enter valua for c:")

#calculate discriminate
discriminant=int(b)**2-4*int(a)*int(c)

#check if the discriminant is negative,positive, or zero
if discriminant>0:
    #calculate the two roots
    root1=(-b+math.sqrt(discriminant)) / (2*a)
    root2=(-b-math.sqrt(discriminant)) / (2*a)
    print("The roots are:",root1,"and",root2)
elif discriminant==0:
    #calculate the single root
    root=-b/(2*a)
    print(root)
else:
    print("There are no roots.")

# calculate area of a circle
r=7
circle=math.pi*r**2
print("The area of the circle is:"+str(circle),"cmsqr")