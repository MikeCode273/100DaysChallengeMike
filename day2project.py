print("Welcome to the tip calculator.")

total_bill = input("What was the total bill? $")

percentage = input("What percentage tip would you like to give? 10, 12, or 15?")

numberofpeople= input("How many people to split the bill? ")

x = float(total_bill)

y= int(percentage)/100

num= int(numberofpeople)

percentoftotal= x * y
add_totalpercent= x + percentoftotal

result = add_totalpercent/num
round_result = round(result,2)
round_result= "{:.2f}".format(result)

print(f"Each person should pay: ${round_result}")