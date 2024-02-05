# an automatic python pizza 

print("Welcome to Python Pizza Delivery\n")

size = input("What size pizza do you want? S or M or L? ")
add_pepperroni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

#conditional rendering: next lines of codes
if size == "S":
    bill +=15
    if add_pepperroni == "Y":
        bill += 2

    if extra_cheese == "Y":
        bill += 1

elif size == "M":
    bill += 20
    if add_pepperroni == "Y":
        bill += 3

    if extra_cheese == "Y":
        bill += 1

elif size == "L":
    bill += 25
    if add_pepperroni == "Y":
        bill += 3

    if extra_cheese == "Y":
        bill += 1

else:
    print("Wrong input.\nPlaese try again!!")





print(f"Your final bill is ${bill}")




