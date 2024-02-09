print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ ''')


import random
Word_list = ["ardvark","baboon","camel"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
random_word = random.choice(Word_list)
word_length=len(random_word)

#set the lives variable to number
lives = 6


random_lst=[]
for _ in range(word_length):
  random_lst+="_"
#print(random_lst)

end_of_game=False
while not end_of_game:
  
  
  guess_character =input("Guess a letter: ").lower()

  
  for char in range(word_length):
    letter=random_word[char]
    # print(f"Current position {char}\n Current letter: {letter}\n Guessed Letter: {guess_character}")
    if letter == guess_character:
      random_lst[char]=letter
      
  
  
#reduce the number of livws 
  if guess_character not in random_word:
    lives-=1

#join all theelements in the list and turn it into a string
  print(f"{' '.join(random_lst)}")

  if "_" not in random_lst:
    end_of_game=True
    print("You win.")
  elif lives==0:
    end_of_game=True
    print("You lose.\nGame Over!!")

#use ascii art to man suicide

 
  print(stages[lives])