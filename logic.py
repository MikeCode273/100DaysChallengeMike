print("Welcome to th rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoster!")
    age= int(input("what is your age?"))
    if age <12:
        bill= 5
        print("Child pay $5.")
    elif age <=18:
        bill= 7
        print("Youth pay $7.") 
    elif age >= 45 and age <= 55:
        print("everything is going to be okay. Have a free ride.")
    else:
        bill = 12
        print("Adult pay $12")

    wants_photo= input("Do you want a photo taken? Y or N: ") 
    if wants_photo == "Y":
        bill += 3
    
    print(f"Your final bill is {bill}")
    
else:
    print("Sorry, you have to grow taller before you can ride.")