  #A laep year challenge 

year_number =int(input("which year do you want to check? "))

if year_number % 4== 0:
    if year_number % 100==0:
        if year_number % 400==0:
            print("leap year")
        else:
            print("Not leap year")
    else:
        print("leap year")
else:
    print("Not leap year.")

