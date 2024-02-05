print("Welcome to the Love Calculator!")

name1 = input("What is your name?\n")
name2 = input("What is their name?\n")
case_name1= name1.lower()
case_name2= name2.lower()

count_name1=case_name1.count('l') + case_name1.count('o') + case_name1.count('v') + case_name1.count('e')
count_name2=case_name2.count('l') + case_name2.count('o') + case_name2.count('v') + case_name2.count('e')

love= count_name1 + count_name2

cover_name1=case_name1.count('t') + case_name1.count('r') + case_name1.count('u') + case_name1.count('e')
cover_name2=case_name2.count('t') + case_name2.count('r') + case_name2.count('u') + case_name2.count('e')

true = cover_name1 + cover_name2

result= int(f"{true}{love}")

if result <= 10 or result >= 90:
    print(f"Your score is {result}%, you go like coke and mentos.")
elif result >= 40 and result <= 50:
    print(f"Your score is {result}%, you are alright together.")
else:
    print(f"Your score is {result}%")