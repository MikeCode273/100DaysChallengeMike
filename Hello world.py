# Program to calculate the weight of any object 
weight=input("weight in grams:")
convert=input("(k)g or (L)bs:")
# Using nested if to convert weiht into either Kg or Pounds

if convert=="k":#if the user input k then it converts the weight into kilograms
    weight_kg= float(weight) / float(0.45)
    print("Weight in kg:"+str(weight_kg)+"kilograms")
    print("Thanks for checking")

elif convert=="l":#if the user input l then it converts the weight into Pounds
    weight_lbs=float(weight)*float(0.45)
    print("Weight in pounds:"+str(weight_lbs)+"Pounds")
else:
    print("Your input is invalid,try again!!")
print("Done")