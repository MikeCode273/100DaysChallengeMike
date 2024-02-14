# # #how to use dictionaries and nested dictionares

# programming_dictionary ={"Bug":"this is that is ","function":"refers to...."}

# # #Retrieving items from dictionary 
# print(programming_dictionary["Bug"])

# # #adding new items to dictionaries
# programming_dictionary["loop"]="The action of doing...."
# # print(programming_dictionary)

# #create an empty dictionary
# # empty_dictionary = {} 

# # empty_dictionary["loop"]="wdmedm"

# # print(empty_dictionary)

# #Edit an item in adictionary
# programming_dictionary["Bug"]= "edit this cieockcmo"

# # print(programming_dictionary)

# #loops in dictionary
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key]) 

#   #Nested dictionary
# capitals = {
#   "France":"Paris",
#   "Germany":"Berlin"
# }



travel_log=[
  {
    "Country":"France",
    "visits":12,
    "cities":["paris","lille","dijon"]
  },
  {
    "Country":"Germany",
    "visits":5,
    "Cities":["Berlin","Hamburg","Stuttgart"]  
  }
]

def add_new_country(Country,visits,cities):
  new_count={}
  new_count["Country"]=Country
  new_count["visits"]=visits
  new_count["Cities"]=cities
  travel_log.append(new_count)

add_new_country("Russia",2,["Moscow","Saint","Petersburg"])
print(travel_log)


#Nesting a dictionary in a list  
