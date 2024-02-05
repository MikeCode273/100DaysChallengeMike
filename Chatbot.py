#a chatBot program

responses={
    "hi":"Hello",
    "how are you?":"I'm doing great by Jehovah's Grace,thanks for asking",
    "what's your name?":"My name is chat Bot,how may i help you?",
    "byeee":"Goodbye!!"
}
#define a function to get a responde to a user input
def get_response(user_input):
    #convert user input into lowercase
    user_input=user_input.lower()
    #Check if the user input is in the responses dictionary
    if user_input in responses:
        return responses[user_input]
    else:
        return "i'm sorry, i don't understand.Please ask me something else."

#main loop to get user input and respond 
while True:
    user_input =input("You:")
    response=get_response(user_input)
    print("Chat Bot:",response)
    #Check if the user input said "byee" at end of the conversation
    if user_input.lower()=="bye":
        break
