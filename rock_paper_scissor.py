import random

rock= 'Rock'
paper = 'Paper'
scissors ='Scissors'

game = [rock,paper,scissors]

choose_choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

 


if choose_choice>=3 or choose_choice<0:
  print("You tyoeed an invalid  number")
else:
  print(f"You chose {game[choose_choice]}")


  computer = random.randint(0,2)
  print(f"Computer choose {game[computer]}")  


  if choose_choice ==0 and computer==2:
    print("You win")
  elif computer==0 and choose_choice==2:
    print("You lose")
  elif computer>choose_choice:
    print('You Lose') 
  elif choose_choice>  computer:
    print("Computer wins.")
  elif computer==choose_choice:
    print("It's a draw")


 

