#function: allows a programmer to reuse a code 

def hello(name, age):
    print("Hello "+ name  +', you are ' + str(age) + " years old")


hello("michael",34)


# return code

def greetings(name):
    if not name:
        return
    print('Hello'+ name + '!')

greetings("mike")

#nest functions
def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')   
    for word in words:
        say(word) 

talk('I am going to buy the milk')


def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count

    return increment    

increment = counter()

print(increment())
print(increment())
print(increment())
print(increment())
