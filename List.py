
import random
#states_of_america = ['Delaware', 'Pensylvinia', 'Brooklyn','Paterson','Chicago']

#print(states_of_america[0])

#states_of_america.append()
#states_of_america.extend() 

names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")

random_index = random.randint(0,len(names)-1)
random_name = names[random_index]


print(f"{random_name} is going to buy the mael today ")