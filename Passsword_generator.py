#Password Generator Project 
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z']
numbers =['0','1','2','3','4','5','6','7','8','9']
symbols =['!','@','#','$','%','&','*','(',')',"+"]

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f'How many symbols woud you like?\n'))
nr_numbers = int(input(f'How many numbers woud you like?\n'))


password_lst = []
for i in range(0,nr_letters):
 password_lst+=random.choice(letters)
#print(password_lst)

for i in range(0,nr_symbols):
 password_lst += random.choice(symbols)
#print(password_lst)

for i in range(0,nr_numbers):
 password_lst += random.choice(numbers)
#print(password_lst)

random.shuffle(password_lst)
#print(password_lst)

password=''
for i in password_lst:
  password+=i
print(f"Your Password is {password}")