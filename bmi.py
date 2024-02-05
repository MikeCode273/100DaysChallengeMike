height = float(input("enter your heith in m: "))
weight = float(input("enter your weight in kg:" ))

bmi_value = round(weight / height ** 2)
print(f"Your BMI value is: {bmi_value}")

if bmi_value < 18.5:
    print("You are Underweight.")
elif bmi_value < 25:
    print("You are normal")
elif bmi_value < 30:
    print("You are overweight")
elif bmi_value < 35:
    print("You are obese")
else:
    print("You are clinically obese")