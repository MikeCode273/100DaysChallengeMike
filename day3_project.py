
print("___Welcome to Treasure Island. Your mission is to find your treasure.___")

start_game= input("Your at a cross road. Where do you want to go? Type \"left\" or \"right\"?\n ").lower

if start_game== "left" :
    island_choice= input("You come to a lake. There is an island in the middle of hte lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across?\n").lower

    if island_choice == "wait":
        door_choose= input("You arrive at the island unharmed.There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n").lower

        if door_choose == "Yellow":
            print("Congratulations. You won!!")
        else:
            print("You enter a room of beasts. Game Over!!")

    else:
        print("Game Over!!")

else:
    print("You fell into the hole. Game Over!!")