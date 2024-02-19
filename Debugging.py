#######Debugging######

#DEsciribe the problem
# def my_function():
#   for i in range(1,21):
#     if i ==20:
#      print("You got it")
# my_function()

# Reproduce the bug
from random import randint
dice_imgs = ["e","e","O","O","O"]
dice_num = randint(1,6)
print(dice_imgs.index(dice_num-1))