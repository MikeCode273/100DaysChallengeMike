#Import necessary libraries 
import math

#Define funtions for Calculator operator
def Add(a,b):
    return a+b

def Subtraction(a,b):
    return a+b

def multiply(a,b):
    return a*b

def Divide(a,b):
    return a/b

def power(a,b):
    return math.pow(a,b)

def square_root(a):
    return math.script(a)

#Define main function for calculator app 
def calculator():
    print("Welcome to th advanced calculator app!")

    print("Please select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3.Multipliction")
    print("4. Division")
    print("5. Power")
    print("6. Square rooot")

choice=input("Enter your choice(1-6)")


#Get user input for nmbers
num1=float(input("Enter first number:")) 
num2=float(input("Enter second number:")) 

#Perform selected operation and display result

if choice=="1":
    print(num1,"+",num2,"=",Add(num1,num2))
elif choice=="2":
    print(num1,"-",num2,"=",Subtraction(num1,num2))
elif choice=="3":
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=="4":
    print(num1,"/",num2,"=",Divide(num1,num2))
elif choice=="5":
    print(num1,"",num2,"=",power(num1,num2))
elif choice=="6":
    print(num1,"",num2,"=",square_root(num1,num2))
else:
    print("Invalid input!!")

   

#Ask the user if they to see another operation
again=input("Do you want to see another operation?(Y/N):")

if again=='Y'or again=='y':
    calculator()
else:
    print("Thank you for using the advance calculator app...")

calculator()