import random

number=random.randint(1,10)
guess=None
count=0

while guess != number:
    guess= int(input("Guess a number between 1 and 10:"))
    count+=1
    if guess>number :
        print("Too low, try again.")
    elif guess >number:
        print("too high, try again.")
    else:
        print("Congratulations, you guessed the right number in",count,"tries.")
