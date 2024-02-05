import random

def get_choices():
    player_choices= input("Enter a choice (Rock,Paper, Scissors): ")
    options= ["rock", "paper", "scissors"] 
    computer_player = random.choices(options)
    choices ={ "player": player_choices, "computer": computer_player}
    return choices


def check_win(player ,computer):
    print(f"You choose:{player}, computer chose:{computer}")
    if player == computer:
        return "It is a tie"
    elif player == "rock":
        if computer=="scissors":
            return "Rock ssamshes scissors! you win!"
        else:
            return "Paper covers rock! You lose!"
    elif player == "paper":
        if computer=="rock":
            return "Paper covers rock! you win!"
        else:
            return "Scissors cuts paper! You lose!"  
    elif player == "scissors":
        if computer=="paper":
            return "Scissors cuts paper! you win!"
        else:
            return "Rock samshes sciccors! You lose!" 
    else:
        return "Sorry you entered a wrong input! Try Again!" 
    
      
choices = get_choices()
result =check_win(choices["player"], choices["computer"])
print(result)







