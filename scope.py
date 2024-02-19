'''#Scope '''

enemies =1

def increace():
  #modifying global variable in with a function
  global enemies
  enemies+=2
  print(f"enemies inside function: {enemies}")
 
increace()
print(enemies)

# #local scope
# def drink_scope():
'''#   #declare variable within the scope
#   #can only accessable inside the function'''
#   potion= 2
#   print(potion)

# drink_scope()

#Global

#declra a variable outside a function
# player_health=10

# def drink_scope():
#   '''declare variable within the scope
#   can only accessable inside the function'''
#   potion= 2
#   print(player_health)

# drink_scope()

#There is no block scope in python
# game_level=3
# def create_enemy():
#   enemies=["SKeleton","Zombie","Alien"]
#   if game_level<3:
#     new_enemy = enemies[0]

#   print(new_enemy)
# create_enemy()

#Global Constants
# PI = 3.13434
# TWITTER_HANDLE = "@yu_angela" 


