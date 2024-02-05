#DATATYPES

#num_char =  len(input("what is your name?"))
#print(int(num_char))
#num =(input("Enter any two digit number:"))
#print(int(num[0])+ int(num[1]))
#PEMDAS = [(),**,*/,+-]
#print(int((3*3)+(3/3)-3))

#EXAMPLE
#height = input("enter your height in m: ")
#weight = input("enter your height in kg: ")
#m= float(height)
#kg = int(weight)
#result = kg /(m*m)
#print(int(result))
#f string

age = input("What is your current age: ")
 
age_ninty = 90 - int(age)
daysleft = 365 * age_ninty
weeksleft = 52 * age_ninty
monthsleft = 12 * age_ninty

print(f"You have {age_ninty} years left.\nYou have {daysleft} days, {weeksleft} weeks, and {monthsleft} months left.")

